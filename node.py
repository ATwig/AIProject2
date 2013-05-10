#node.py
#
#Cameron Burton
#Dennis Honeyman

import math

LEARNING_RATE = 0.1

class Node:

    def __init__(self, parents):
        self.parents = parents
        if parents != []:
            for parent in parents:
                parent[0].children.append(self)
        self.defaultOutput = 1
        self.activationValue = 0
        self.error = None
        self.correctValue = None
        self.children = []

    def calcError(self):
        if self.error is not None:
            return self.error
        if self.children == []:
            #output calculation
            pass
        else:
            #hidden calculation
            pass
        #self.error = dsafa

    def compute(self):
        if self.parents == []:
            return self.defaultOutput

        self.activationValue = 0
        for parent in self.parents:
            self.activationValue += parent[1] * parent[0].compute()
        return self.activationFn(self.activationValue)

    def activationFn(self, num):
        return 1 / (1 + math.e ** (-1 * num))

    def updateWeights(self):
        for parent in parents:
            parent[1] += LEARNING_RATE * self.activationValue * self.calcError()

        for parent in parents:
            parent[0].updateWeights()

    def updateError(self):
        if self.correctValue == None:
            print "ERROR: Set correctValue before updating errors!"
            return
        self.calcError()
        if(self.parents != []):
            for i in parents:
                i[0].updateError()

    def reset(self):
        self.defaultOutput = 1
        self.activationValue = 0
        self.error = None
        self.correctValue = None

        for parent in parents:
            parent[0].reset()

    def activationFnDeriv(self, num):
        return num * (1 - num)

    def getDepth(self):
        if self.children == []:
            return 0
        depth = 0
        curNode = self
        while(True):
            depth += 1
            curNode = curNode.children[0]
            if curNode.children == []:
                break

        return depth

    def __str__(self):
        if self.parents == []:
            return "[PARENT]"
        return "[NODE]\n" + "".join(
                map(lambda x: "%s(%s) %s\n" % ("  " * x[0].getDepth(), x[1], x[0]), self.parents))
