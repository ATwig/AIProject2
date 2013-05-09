#node.py
#
#Cameron Burton
#Dennis Honeyman

class Node:

    def __init__(self, parents):
        self.parents = parents
        if parents != []:
            for parent in parents:
                parent[0].children.append(self)
        self.children = []

    def getError(self):
        #return error
        print "test"

    def compute(self):
        #return computed value
        print "test"

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
