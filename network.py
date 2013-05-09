import random
import cPickle

from node import *;

class Network:
    def __init__(self):
        self.symInputNode = Node([])
        self.ecInputNode = Node([])

        hiddenLayer = []
        for i in range(0, 5):
            hiddenLayer.append(Node([
                (self.symInputNode, random.random()),
                (self.ecInputNode, random.random()),
                (Node([]), random.random()),
                ]))

        self.boltNode = Node(map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5)))
        self.nutNode = Node(map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5)))
        self.ringNode = Node(map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5)))
        self.scrapNode = Node(map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5)))


    def PrintNetwork(self):
        for node in [self.boltNode, self.nutNode, self.ringNode, self.scrapNode]:
            print str(node)

    def TrainNetwork(self, trainingData, epochs, weightFilename, imageFilename):
        #todo
        pass

    def TestNetwork(self, testData, trainedWeightsFilename, classificationRegionFilename):
        data = cPickle.load(trainedWeightsFilename)
        self.boltNode = data[0]
        self.nutNode = data[1]
        self.ringNode = data[2]
        self.scrapNode = data[3]

        #TODO: Test
