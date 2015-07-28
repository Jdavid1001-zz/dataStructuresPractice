# -*- coding: utf-8 -*-
import copy
class StringBucket:
    """
    Abstract class for a string hash table's bucket. It only implements all necessary 
    functions to work as a bucket for a hash table. Also, includes a few 
    private data members, both class and instance, to help these functions.
    """ 
    
    def __init__(self, maxCollisions = -1):
        self.index = 0
        self.__maxCol = maxCollisions
        self.__numItems = 0
        
    def __iter__(self):
        self.index = 0        
        
    def next(self):
        self.index = 0
        raise StopIteration
    
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
    def __init__(self, hashFunction, bucketType, minNumBuckets = 1, maxCollisions = -1, willFill = False, loadFactorThresh = 1.5):
        self.willFill = willFill
        self.loadFactorThresh = 1.5
        self.index = 0
        self.bucketType = bucketType
        self.maxCol = maxCollisions
        self.hashFunc = hashFunction
        self.lBuckets = [bucketType(maxCollisions) for x in range(minNumBuckets)]
        self.numBuckets = minNumBuckets
        pass

    def __iter__(self):
        self.index = 0
        return self
        
    def next(self):
        while (self.index < self.numBuckets):
            try:
                return self.lBuckets[self.index].next()
            except StopIteration:
                self.index += 1
        raise StopIteration

    def grow(self):
        tempBuckets = copy.deepcopy(self.lBuckets)
        self.numBuckets *= 2
        self.lBuckets = [self.bucketType(self.maxCol) for x in range(self.numBuckets)]
        for bucket in tempBuckets:
            iter(bucket)
            while True:
                try:
                    key, val = bucket.next
                    self.insert(key, val)
                except StopIteration:
                    iter(bucket)
                    break

    def loadFactor(self):
        return float(self.numItems)/self.numBuckets
        
    def isTooFull(self):
        if self.willFill and self.loadFactor() > self.loadFactorThresh:
            return True
        else:
            return False
    
    def insert(self, key, value):
        if self.isTooFull:
            self.grow()
        hashedKey = self.hashFunc(key)
        i = hashedKey % self.numBuckets
        wasInserted = self.lBuckets[i].insert(key, value)
        if wasInserted == -1:
            self.grow()
            
    def numItems(self):
        return sum([b.getNumItems for b in self.lBuckets])