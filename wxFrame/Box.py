from Grid import Grid
import wx

''' A class for coloring in Grid coordinates '''

class Box(wx.Panel):
    Speed = 300
    ID_TIMER = 1
    def __init__(self, parent, id, grid, callbackFcn):
            wx.Panel.__init__(self, parent, id)
            #wx.Color.__init__(self, parent, id)
            self.timer = wx.Timer(self, Box.ID_TIMER)
            self.callbackFcn = callbackFcn
            self.xCoord = 0
            self.yCoord = 0
            self.xWidth = 0
            self.yHeight = 0
            self.grid = grid
            self.Bind(wx.EVT_TIMER, self.OnTimer, id=Box.ID_TIMER)

    def OnTimer(self, event):
        if event.GetId() == Box.ID_TIMER:
           self.callbackFcn()
           self.Refresh()
        else:
            event.Skip()    
    
    def Draw(self, grid, xCoord, yCoord, xWidth, yHeight):
        self.Bind(wx.EVT_PAINT, lambda event: self.OnPaint(event, grid, xCoord, yCoord, xWidth, yHeight))

    def OnPaint(self, evt, grid, xCoord, yCoord, xWidth, yHeight):        
        self.dc = wx.PaintDC(self)
        self.dc.BeginDrawing()
        while (yCoord  < grid.getColLength()):
            while (xCoord < grid.getRowLength()):
                # Note: Need to translate grid values -> color gradient grid.value => grid.color
                value = grid.getValue(xCoord, yCoord)
                color = wx.Colour(value, value, value)
                self.DrawSquare(xCoord*xWidth, yCoord*yHeight, xWidth, yHeight, color)
                xCoord += 1
            xCoord = 0
            yCoord += 1
        self.dc.EndDrawing()
        del self.dc

    def DrawSquare(self, xCoord, yCoord, xWidth, yHeight, color):
        self.dc.SetPen(wx.Pen("black", style=wx.TRANSPARENT))
        self.dc.SetBrush(wx.Brush(color, wx.SOLID))
        self.dc.DrawRectangle(xCoord, yCoord, xWidth, yHeight)

    # Converts a value in the range (0 - 255) inclusive into a greyscale color 
    # based on the value intensity
    def convertGrey(self, value):
        return 0

    def getXWidth(self):
        return self.XWidth
  
    def setXWidth(self, width):
        self.XWidth = width
             
    def getYHeight(self):
        return self.YWidth
      
    def setYHeight(self, height):
        self.YHeight


