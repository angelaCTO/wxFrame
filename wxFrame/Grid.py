import random
import time
import threading
import Buffer


class Grid:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.length = r * c
        self.buffer = [0] * self.length
        self.maxSet = False
        self.avgSet = False
        # For testing ...
        self.counter = 0
        self.colorValue = 0

    def updateBuffer(self):
        tempBuffer = Buffer.getBuffer()

        print "Temp", len(tempBuffer)
        print tempBuffer[0]
        for y in range (self.column):
            for x in range (self.row):
                _value = tempBuffer[x * self.column + y]
                self.setValue(x,self.column - y - 1,_value)

    def genRandGridTest(self):
        for y in range (self.column):
            for x in range (self.row):
                _value = random.randrange(0,255,1)
                _x = random.randrange(0,self.row,1)
                _y = random.randrange(0,self.column,1)
                self.setValue(_x,_y,_value)

    def getRowLength(self):
        return self.row

    def getColLength(self):
        return self.column

    def getValue(self,r,c):
        return self.buffer[r * self.column + c]
    
    def setValue(self, r, c, value):
        self.buffer[r * self.column + c] = value
        self.maxSet = False;
        self.avgSet = False;
    
    def updateMaxInformation(self):
        maxIndex = self.buffer.index(max(self.buffer)) 
        self.maxRowIndex    = maxIndex / self.column
        self.maxColumnIndex = maxIndex % self.column
        self.maxSet = True

    def getMax(self): # Does this get max value ?
        return max(self.buffer)

    def getMin(self):
        return min(self.buffer)

    def getAvg(self) :
        return sum(self.buffer) / len (self.buffer) 
    
    def getMaxRowIndex(self):
        maxIndex = self.buffer.index(max(self.buffer)) 
        self.maxRowIndex    = maxIndex / self.column
    
    def getMaxColumnIndex(self):
        maxIndex = self.buffer.index(max(self.buffer)) 
        self.maxRowIndex    = maxIndex % self.column

    def gridAddition(self,inputGrid):
        if self.row != inputGrid.row or self.column != inputGrid.column:
            return False
        else :
            self.buffer = [x + y for x, y in zip(self.buffer, inputGrid.buffer)]
        return True
    
    def gridScalarAddition(self, scalar):
        self.buffer = [x+scalar for x in self.buffer]

    def gridScalarMultiplication(self, scalar):
        self.buffer = [x*scalar for x in self.buffer]
