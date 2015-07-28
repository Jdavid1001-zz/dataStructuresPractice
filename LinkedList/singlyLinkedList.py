# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/JuanDa/Documents/Spyder Workspace/Interview Prep/dataStructures/Hash')
from MyHashBase import StringBucket

class SuperNode(StringBucket):
    def __init__(self, key = None, value = None, nextNode = None, prevNode = None):
        self.nextNode = nextNode
        self.prevNode = prevNode
        self.key = key
        self.val = value
    
    def getData(self):
        return (self.key, self.val)
        
    def getKey(self):
        return self.key
    
    def getVal(self):
        return self.val

    
class SinglyLinkedNode(SuperNode):
    def setNextNode(self, newNextNode):
        self.next = newNextNode
        return self.next
        
    def getNextNode(self):
        return self.nextNode
    
    
class SinglyLinkedList(StringBucket):
    def __init__(self, maxCollisions = -1):
        super(self.__class__, self).__init__()
        self.head = None
        
    def search(self, key):
        if not self.head:
            return False
        else:
            currNode = self.head
            while key!= currNode.getKey and currNode.getNextNode:
                currNode = currNode.getNextNode
            if currNode.getKey:
                return True
            else:
                return False
    
    def delete(self, key):
        pass
        
    def setKeyVal(self, key, val):
        if not self.head:
            self.head = SinglyLinkedNode(key, val)
        else:
            currNode = self.head
            collisions = 1
            while currNode.getNextNode:
                currNode = currNode.getNextNode
                collisions += 1
            currNode.setNextNode(SinglyLinkedNode(key, val))

    def next(self):
        self.index = 0
        raise StopIteration