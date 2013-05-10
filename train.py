#train.py
#
#Cameron Burton
#Dennis Honeyman

import sys
import csv
import cProfile
from pylab import *

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
    net.TrainNetwork(trainingData, 300, "network%s.pickle" %5, "test5.png")
    net.PrintNetwork()


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
    #cProfile.run('main()')
