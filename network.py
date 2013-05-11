import cPickle
import random

from node import *;

class Network:
    def __init__(self):
        def randomWeight():
            return random.randrange(-1, 1)

        self.symInputNode = Node("sym", [])
        self.ecInputNode = Node("ec", [])

        hiddenLayer = []
        for i in range(0, 5):
            hiddenLayer.append(Node("hidden%s" % i, [
                [self.symInputNode, randomWeight()],
                [self.ecInputNode, randomWeight()],
                [Node("bias%s" % i, []), randomWeight()],
                ]))
        hiddenLayer.append(Node("biasOutput", []))

        self.boltNode = Node("bolt", map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,6)))
        self.nutNode = Node("nut", map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,6)))
        self.ringNode = Node("ring", map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,6)))
        self.scrapNode = Node("scrap", map(lambda x, y: [x, randomWeight()], hiddenLayer, range(0,6)))

        self.outputNodes = [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]
        self.profit = 0
        self.numErrors = 0
        self.results = []
        

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
        cPickle.dump(self, file(weightFilename, 'w'))


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
            
            self.results.append((int(maxIndex+1), int(entry[2])))
            
            if maxIndex+1 == entry[2]:
                #print "Match!\n"
                
                if entry[2] == 1:
                    self.profit += 0.20
                elif entry[2] == 2:
                    self.profit += 0.15
                elif entry[2] == 3:
                    self.profit += .05
                else:
                    self.profit -= 0.03
                
            else:
                #print "Wrong: %s vs %s" % ((maxIndex+1), entry[2])
                #for n in self.outputNodes:
                    #print n.output
                    
                #print "-----\n"
            
                self.numErrors +=  1
                
                if maxIndex+1 == 4:
                    self.profit -=0.03
                else:
                    self.profit -=0.07
            
            #self.PrintNetwork();

            for node in self.outputNodes:
                node.reset()
        #end for each loop
       # print len(testData)
        print "Number of Errors: %s" % self.numErrors
        print "Percentage wrong: %s" % ((float(self.numErrors) / len(testData)) * 100)
        print "Total Profit: %s" % self.profit
        self.makeHistogram()
        
    def makeHistogram(self):
        
        outputValues = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        for r in self.results:
            #print r
            outputValues[r[0]-1][r[1]-1] += 1
            
        print "               Output Class"
        print "Expected Class   1  2  3  4"
        i = 1
        for o in outputValues:
            print "              %s %s" % (i, o)
            i+= 1
            
            
        
        
        
        