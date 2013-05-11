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


def main():
    if len(sys.argv) != 2:
        print "Error, wrong number of arguments"
        return

    trainingData = getTrainingData(sys.argv[1])

    net = Network()
    for i in [0, 10, 100, 1000, 10000]:
        net.TrainNetwork(trainingData, i, "network%s.pickle" % i, "test%s.png" % i)


if __name__ == "__main__":
    main()
