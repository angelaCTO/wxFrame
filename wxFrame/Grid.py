# author: Samuel Chen

class Grid:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.length = r * c
        self.buffer = [0] * self.length
        self.maxSet = False
        self.avgSet = False

    #
    def getRowLength(self):
        return self.row

    #
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

