#train.py
#
#Cameron Burton
#Dennis Honeyman

import sys
import csv

from network import *
from node import *


def getTrainingData(trainingFile):

    trainingData = []

    with open (trainingFile, 'rb') as csvfile:
        inReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in inReader:
            tempRow = [float(i) for i in row]
            trainingData.append(tempRow)

    return trainingData


def outputTree(trainedNet):
    #use pickle?
    print "out"


def main():
    if len(sys.argv) != 2:
        print "Error, wrong number of arguments"
        return

    trainingData = getTrainingData(sys.argv[1])

    net = Network()
    for i in [0, 10, 100, 1000, 10000]:
        net.TrainNetwork(trainingData, i, "network%s.pickle" % i, "test%s.png" % i)


def testNetwork():
    net = Network()
    net.PrintNetwork()

def testNodes():
    p1 = Node([])
    p1.defaultOutput = 0
    p2 = Node([])
    p2.defaultOutput = 1
    p3 = Node([])
    p3.defaultOutput = 1

    node = Node([(p1, 0.3), (p2, 0.6), (p3, 0.8)])
    print node.compute()


if __name__ == "__main__":
    main()
