#train.py
#
#Cameron Burton
#Dennis Honeyman

import node
import sys
import csv

def trainNetwork(training_data, network):
    #Function returns a list of the networks at each epoch
    #Eg: trainedNetwork[0] is the network after 10 epochs,
    #     trainedNetwork[1] is the network after 100 epochs, Etc.
    
    
    epochs = 0
    trainedNetwork = []
    
    
def getTrainingData(trainingFile):
    
    trainingData = []
    
    with open (trainingFile, 'rb') as csvfile:
        inReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in inReader:
            tempRow = [float(i) for i in row]
            trainingData.append(tempRow)
    
    for i in trainingData:
        print i

    return trainingData
        
def outputTree(trainedNet):
    #use pickle?
    print "out"
    
	
def main():
    if len(sys.argv) != 2:
        print ("Error, wrong number of arguments")
        return
        
    trainingData = getTrainingData(sys.argv[1])
    
    #trainedNetworks = trainNetwork(training_data)


main()
