import cPickle
import random
import pylab as p

from node import *;

class Network:
    def __init__(self):
        def randomWeight():
            return random.randrange(-1, 1)

        self.symInputNode = Node("sym", [])
        self.ecInputNode = Node("ec", [])

        self.hiddenNodes = []
        for i in range(0, 5):
            self.hiddenNodes.append(Node("hidden%s" % i, [
                [self.symInputNode, randomWeight()],
                [self.ecInputNode, randomWeight()],
                [Node("bias%s" % i, []), randomWeight()],
                ]))
            outputParents = self.hiddenNodes + [Node("biasOutput", [])]

        self.boltNode = Node("bolt", map(lambda x, y: [x, randomWeight()], outputParents, range(0,6)))
        self.nutNode = Node("nut", map(lambda x, y: [x, randomWeight()], outputParents, range(0,6)))
        self.ringNode = Node("ring", map(lambda x, y: [x, randomWeight()], outputParents, range(0,6)))
        self.scrapNode = Node("scrap", map(lambda x, y: [x, randomWeight()], outputParents, range(0,6)))

        self.outputNodes = [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]


    def PrintNetwork(self):
        #for node in [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]:
        for node in [self.boltNode]:
            print str(node)

    def TrainNetwork(self, trainingData, epochs, weightFilename, imageFilename):
        p.xlabel("number of epochs")
        p.ylabel("SSE")
        sseList = []

        for i in range(epochs):
            sse = 0
            for entry in trainingData:
                self.symInputNode.output = entry[0]
                self.ecInputNode.output = entry[1]

                self.boltNode.compute()
                self.nutNode.compute()
                self.ringNode.compute()
                self.scrapNode.compute()

                expected_result = [0]*4
                expected_result[int(entry[2]) - 1] = 1

                for node, value in zip(self.outputNodes, expected_result):
                    node.correctValue = value

                for node in self.outputNodes:
                    node.updateError()

                for node in self.outputNodes:
                    sse += node.error**2

                self.boltNode.updateWeights(True)
                self.nutNode.updateWeights(False)
                self.ringNode.updateWeights(False)
                self.scrapNode.updateWeights(False)

                for node in self.outputNodes + self.hiddenNodes:
                    node.reset()

            sseList.append(sse)

        p.plot(range(epochs), sseList)
        cPickle.dump(self, file(weightFilename, 'w'))
        p.savefig(imageFilename)

    def TestNetwork(self, testData, classificationRegionFilename):
        for entry in testData:
            self.symInputNode.output = entry[0]
            self.ecInputNode.output = entry[1]

            self.boltNode.compute()
            self.nutNode.compute()
            self.ringNode.compute()
            self.scrapNode.compute()

            maxIterator = 0
            maxIndex = 0
            maxValue = 0
            while maxIterator < 4:
                if maxValue < self.outputNodes[maxIterator].output:
                    maxValue = float(self.outputNodes[maxIterator].output)
                    maxIndex = int(maxIterator)

                maxIterator += 1

            if maxIndex+1 == entry[2]:
                print "Match!\n"
            else:
                print "Wrong: %s vs %s" % ((maxIndex+1), entry[2])
                for n in self.outputNodes:
                    print n.output

                print "-----\n"

            #self.PrintNetwork();

            for node in self.outputNodes:
                node.reset()

    def GetResult(self, rotationalSymmetry, eccentricity):
        self.symInputNode.output = rotationalSymmetry
        self.ecInputNode.output = eccentricity

        self.boltNode.compute()
        self.nutNode.compute()
        self.ringNode.compute()
        self.scrapNode.compute()

        maxValue = max(map(lambda x: x.output, self.outputNodes))
        return [x[1] for x in
                zip(self.outputNodes, range(len(self.outputNodes)))
                if x[0].output == maxValue][0]


    def WriteClassificationRegion(self, imageFilename):
        p.xlabel("eccentricity")
        p.ylabel("rotational symmetry")
        points = [[[], []], [[], []], [[], []], [[], []]]
        for ecc in p.arange(0.0, 1.0, 0.02):
            for rotsym in p.arange(0.0, 1.0, 0.02):
                resultClass = self.GetResult(rotsym, ecc)
                points[resultClass][0].append(ecc)
                points[resultClass][1].append(rotsym)

        for point, color in zip(points, ["ro", "bo", "go", "yo"]):
            p.plot(point[0], point[1], color)
        p.legend(("Bolt", "Nut", "Ring", "Scrap"),
                loc='upper right',
                shadow=True,
                fancybox=True)
        p.savefig(imageFilename)
