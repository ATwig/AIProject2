import random

from node import *;

class Network:
    def __init__(self):
        def randomWeight():
            return random.randrange(-1, 1)

        self.symInputNode = Node([])
        self.ecInputNode = Node([])

        hiddenLayer = []
        for i in range(0, 5):
            hiddenLayer.append(Node([
                [self.symInputNode, randomWeight()],
                [self.ecInputNode, randomWeight()],
                [Node([]), randomWeight()],
                ]))

        self.boltNode = Node(map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,5)))
        self.nutNode = Node(map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,5)))
        self.ringNode = Node(map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,5)))
        self.scrapNode = Node(map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,5)))

        self.outputNodes = [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]


    def PrintNetwork(self):
        #for node in [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]:
        for node in [self.boltNode]:
            print str(node)

    def TrainNetwork(self, trainingData, epochs, weightFilename, imageFilename):
        for i in range(epochs):
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

                self.boltNode.updateWeights(True)
                self.nutNode.updateWeights(False)
                self.ringNode.updateWeights(False)
                self.scrapNode.updateWeights(False)

                #self.PrintNetwork();

                for node in self.outputNodes:
                    node.reset()

                #self.PrintNetwork();


    def TestNetwork(self, testData, trainedWeightsFilename, classificationRegionFilename):
        #TODO: Test
        pass
