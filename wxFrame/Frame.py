#! /usr/bin/python
from Grid import Grid
from Box import Box
import wx
import time

''' A simple test driver for Frame/Grid program '''

X_COORD = 0            # Where to start coloring on Grid
Y_COORD = 0            
BOX_WIDTH = 10         # Dimensions of Grid boxes
BOX_HEIGHT = 10

def main():
    app = wx.App()
    frame = wx.Frame(None, -1, 'TestFrame.py')

    grid = Grid(32,31)
    box = Box(frame, -1, grid, grid.toggleGridTest)
    #box = Box(frame, -1, grid, grid.genRandGridTest)

    print '1'
    box.timer.Start()
     
    print '2' 
    grid.toggleGridTest()
    #grid.genRandGridTest()
    box.Draw(grid,X_COORD,Y_COORD,BOX_WIDTH,BOX_HEIGHT)
     
    print '3' 
    frame.Show(True)
    print '4'
    app.MainLoop()
    print '5'
        
# Start
if __name__ == '__main__':
    main()

