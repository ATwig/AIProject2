#node.py
#
#Cameron Burton
#Dennis Honeyman

import math

LEARNING_RATE = 0.9

class Node:

    def __init__(self, name, parents):
        self.parents = parents
        if parents != []:
            for parent in parents:
                parent[0].children.append(self)
        self.output = 1
        self.name = name
        self.activationValue = 0
        self.error = None
        self.correctValue = None
        self.children = []

    def calcError(self):
        if self.children == []:
            #output calculation
            self.error = self.activationFnDeriv(self.output) * (self.correctValue - self.output)
        else:
            #hidden calculation
            sumOfChildError = 0
            for child in self.children:
                if child.error is None:
                    child.calcError()
                for i in child.parents:
                    if i[0] == self:
                        sumOfChildError += child.error * i[1]
            self.error = self.activationFnDeriv(self.output) * sumOfChildError

    def compute(self):
        if self.parents == []:
            return self.output

        self.activationValue = 0
        for parent in self.parents:
            self.activationValue += parent[1] * parent[0].compute()
        self.output = self.activationFn(self.activationValue)
        return self.output

    def activationFn(self, num):
        return 1 / (1 + math.e ** (-num))

    def updateWeights(self, recursively):
        for parent in self.parents:
            parent[1] += LEARNING_RATE * parent[0].output * self.error

        if not recursively:
            return

        for parent in self.parents:
            parent[0].updateWeights(True)

    def updateError(self):
        if self.correctValue == None and self.children == []:
            print "ERROR: Set correctValue before updating errors!"
            return
        self.calcError()
        for i in self.parents:
            i[0].updateError()

    def reset(self):
        self.output = 1
        self.activationValue = 0
        self.error = None
        self.correctValue = None

        for parent in self.parents:
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
            return "[%s]" % self.name
        return ("[err:%s %s]\n" % (self.error, self.name)) + "".join(
                map(lambda x: "%s(weight: %s) %s\n" % ("  " * x[0].getDepth(), x[1], x[0]), self.parents))
