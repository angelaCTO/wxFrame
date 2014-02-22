from Grid import Grid
import wx

''' A class for coloring in Grid coordinates '''

class Box(wx.Panel):
    def __init__(self, parent, id, grid):
            wx.Panel.__init__(self, parent, id)
            self.xCoord = 0
            self.yCoord = 0
            self.xWidth = 0
            self.yHeight = 0
            self.grid = grid
        
    def Draw(self, grid, xCoord, yCoord, xWidth, yHeight):
        self.Bind(wx.EVT_PAINT, lambda event: self.OnPaint(event, grid, xCoord, yCoord, xWidth, yHeight))

    def OnPaint(self, evt, grid, xCoord, yCoord, xWidth, yHeight):        
        self.dc = wx.PaintDC(self)
        self.dc.BeginDrawing()
        while (yCoord  < grid.getColLength()):
            while (xCoord < grid.getRowLength()):
                # Note: Setting color diff for testing purposes
                # Note: Need to translate grid values -> color gradient grid.value => grid.color
                if (grid.getValue(xCoord, yCoord) == 0):
                    color = "black"
                else:
                    color = "white"
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

    def getXWidth(self):
        #xwidth = self.GetClientSize().GetWidth()
        return self.XWidth
  
    def setXWidth(self, width):
        self.XWidth = width
        
    def getYHeight(self):
        return self.YWidth
      
    def setYHeight(self, height):
        self.YHeight



