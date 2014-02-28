import random

class Grid:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.length = r * c
        self.buffer = [0] * self.length
        self.maxSet = False
        self.avgSet = False
        self.counter = 0

    # Sets grid element values to alterate between 0 and 1 
    # for testing
    def toggleGridTest(self):
        if self.counter == 0 :
            # Set alternating grid
            for y in range (self.column):
                for x in range (self.row):
                    if (x % 2 == 0 and y % 2 == 0):
                        self.setValue(x,y,0)
            self.counter = 1
        else :
            for y in range (self.column):
                for x in range (self.row):
                    if (x % 2 == 0 and y % 2 == 0):
                        self.setValue(x,y,1)
            self.counter = 0

    # Test to generate random Grid
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

    def getMax(self):
        return max(self.buffer)

    def getMin(self):
        return min(self.buffer)

    # Converts value to greyscale
    def getGrey(self, value):
        # Convert singular value to RGB scale
        _max = self.getMax()
        _min = self.getMin()
      
       # Convert RGB to grayscale 
       # return (0.21*R + 0.71*G + 0.07*B)
    
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
