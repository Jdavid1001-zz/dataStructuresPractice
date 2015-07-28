# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/JuanDa/Documents/Spyder Workspace/Interview Prep/dataStructures/Hash')
from MyHashBase import StringBucket
from MyHashBase import StringHashTable

class SuperNode(StringBucket):
    def __init__(self, keyValTuple = None, nextNode = None, prevNode = None, maxCollisions = -1):
        super(self.__class__,self).__init__(maxCollisions)
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.data = keyValTuple
    
class SinglyLinkedList(StringHashTable):
    def __init__(self):
        super(self.__class__, self).__init__()
        
