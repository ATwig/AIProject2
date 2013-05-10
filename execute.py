#execute.py
#
#Cameron Burton
#Dennis Honeyman

import cPickle
import sys

from network import *
from node import *

def main():
    if len(sys.argv) != 2:
        print "Error, wrong number of arguments"
        return

    net = cPickle.load(sys.argv[1])
    #TODO: Run testing functions
    pass

if __name__ == '__main__':
    main()
