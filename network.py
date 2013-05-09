import random

from node import *;

class Network:
	def __init__(self):
		self.symInputNode = Node(None)
		self.ecInputNode = Node(None)

        hiddenLayer = []
        for i in range(0, 5):
            hiddenLayer += Node([
                (self.symInputNode, random.random()),
                (self.ecInputNode, random.random()),
                (Node(None), random.random()),
                ])
		
        self.boltNode = map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5))
        self.nutNode = map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5))
        self.ringNode = map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5))
        self.scrapNode = map(lambda x, y: (x, random.random()), hiddenLayer, range(0,5))

		
    def TrainNetwork(self, trainingData, epochs, weightFilename, imageFilename):
        #todo
        pass

    def TestNetwork(self, testData, classificationRegionFilename):
        #todo
        pass
