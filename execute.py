#execute.py
#
#Cameron Burton
#Dennis Honeyman

import cPickle
import sys
import csv

from network import *
from node import *

def getData(dataFile):

    trainingData = []

    with open (dataFile, 'rb') as csvfile:
        inReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in inReader:
            tempRow = [float(i) for i in row]
            trainingData.append(tempRow)

    return trainingData


# def main():
	# testDataList = []
	
    # if len(sys.argv) != 3:
        # print "Error, wrong number of arguments"
        # return

	# net = cPickle.load(file(sys.argv[2], 'r'))	
	
	# testDataList = self.getData(sys.argv[1])
    
    ##TODO: Run testing functions
    # net.TestNetwork(testDataList, "")


def main():
	testDataList = []
	
	if len(sys.argv) != 3:
		print "Error, wrong number of args"
		return
		
	net = cPickle.load(file(sys.argv[2], 'r'))
	
	testDataList = getData(sys.argv[1])
	
	net.TestNetwork(testDataList, "")
if __name__ == '__main__':
    main()
