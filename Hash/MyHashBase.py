# -*- coding: utf-8 -*-

class StringBucket:
    """
    Abstract class for a string hash table's bucket. It only implements all necessary 
    functions to work as a bucket for a hash table. Also, includes a few 
    private data members, both class and instance, to help these functions.
    """ 
    
    def __init__(self, maxCollisions = -1):
        self.__maxCol = maxCollisions
        self.__numItems = 0
    
    def setKeyVal(key, val):
        return 0
    
    def insert(self, key, val):
        wasInserted = self.setKeyVal(key, val) #Zero means value was not inserted
        if wasInserted == 1: #Was inserted perfectly
            self.__numItems += 1
        if self.__maxCol != -1 and self.__numItems > self.__maxCol:
            return -1
        return wasInserted

    def search(self, key):
        pass
    
    def delete(self):
        pass
    
    def getNumItems(self):
        return self.__numItems
    
class StringHashTable:
    def __init__(self, hashFunction, bucketType, minNumBuckets = 1, maxCollisions = -1):
        self.hashFunc = hashFunction
        self.lBuckets = [bucketType(maxCollisions) for x in range(minNumBuckets)]
        self.numBuckets = minNumBuckets
        pass

    def grow():
        pass
    
    def insert(self, key, value):
        hashedKey = self.hashFunc(key)
        i = hashedKey % self.numBuckets
        wasInserted = self.lBuckets[i].insert(key, value)
        if wasInserted == -1:
            self.grow()
            
    def numItems(self):
        return sum([b.getNumItems for b in self.lBuckets])
    
    def enumerateItems():
        pass