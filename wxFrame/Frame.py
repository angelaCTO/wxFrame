#/usr/bin/python
from Grid import Grid
from Box import Box
import wx
import time
import Udp
import Buffer
''' A simple test driver for Frame/Grid program '''

X_COORD = 0            # Where to start coloring on Grid
Y_COORD = 0            
BOX_WIDTH = 10         # Dimensions of Grid boxes
BOX_HEIGHT = 10
ROW = 31
COLUMN = 32

def main():
    global ROW
    global COLUMN

    Buffer.initBuffer(ROW * COLUMN)

    grid = Grid(ROW,COLUMN)

    Udp.init()

    app = wx.App()
    frame = wx.Frame(None, -1, 'TestFrame.py')

    box = Box(frame, -1, grid, grid.updateBuffer)

    box.timer.Start(10)  # Frame Rate 5 miliseconds

    box.Draw(grid,X_COORD,Y_COORD,BOX_WIDTH,BOX_HEIGHT)
     
    frame.Show(True)
    app.MainLoop()
        
# Start
if __name__ == '__main__':
    main()

