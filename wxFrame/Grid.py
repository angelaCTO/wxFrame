import random
import time

class Grid:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.length = r * c
        self.buffer = [0] * self.length
        self.maxSet = False
        self.avgSet = False
        self.counter = 0
        self.colorValue = 0

    # Sets grid element values to alterate between 0 and 1 
    # for testing
    def toggleGridTest(self):
        if self.counter == 0 :
            # Set alternating grid
            for y in range (self.column):
                for x in range (self.row):
                    if ((x % 2 == 0) and (y % 2 == 0)):
                        self.setValue(x,y,0)
                    if ((x % 2 == 1) and (y % 2 == 1)):
                        self.setValue(x, y, 1)
            self.counter = 1
        else :
            for y in range (self.column):
                for x in range (self.row):
                    if ((x % 2 == 0) and (y % 2 == 0)):
                        self.setValue(x,y,1)
                    if ((x % 2 == 1) and (y % 2 == 1)):
                        self.setValue(x, y, 1)
            self.counter = 0

    def genRandGridTest(self):
        for y in range (self.column):
            for x in range (self.row):
                _value = random.randrange(0,255,1)
                _x = random.randrange(0,self.row,1)
                _y = random.randrange(0,self.column,1)
                self.setValue(_x,_y,_value)
        print "grid id: ", random.randrange(0,100,1)

    # Incrementing value should change color value from 
    # black to white
    def incrementValueTest(self):
        if (self.colorValue < 255):
            print "color value: ", self.colorValue
            self.setValue(1, 0, self.colorValue)
            self.setValue(0, 1, self.colorValue)
            self.setValue(23, 5, self.colorValue)
            self.setValue(10, 20, self.colorValue)
            self.setValue(29, 30, self.colorValue)
            self.setValue(21, 12, self.colorValue)
            self.setValue(15, 26, self.colorValue)
            self.setValue(0, 19, self.colorValue)
            self.setValue(23, 8, self.colorValue)
            self.colorValue += 10
        else:
            self.colorValue = 0
        
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

    # Converts value to RGB tuple
    def getRGB(self, value):
        rgb = (value, value, value)
        return rgb
        #return (0.21*R + 0.71*G + 0.07*B)
    
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
