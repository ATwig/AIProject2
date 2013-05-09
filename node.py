#node.py
#
#Cameron Burton
#Dennis Honeyman

class Node:

    def __init__(self, parents):
        self.parents = parents;
        self.children = None;
        self.weight = 0;
        
    def getError():
        #return error
        print "test"
        
    def compute():
        #return computed value
        print "test"

#end Node

class Network:
	def __init__(self):
		self.symInputNode = Node(None)
		self.ecInputNode = Node(None)
		
		self.one = (symInputNode, ecInputNode)
		self.two = (symInputNode, ecInputNode)
		self.three = (symInputNode, ecInputNode)
		self.four = (symInputNode, ecInputNode)
		self.five = (symInputNode, ecInputNode)
		
		#self.outOne = list of previous nodes
		#self.outTwo
		#self.outThree
		#self.outFour
		
		#self.biasOne
		#self.biasTwo
		
		#need to figure out a way to set children, or do
		# we just manually assign each of them...?
		
		