#! /usr/bin/python
import wx
from Grid import Grid
from Box import Box

''' A simple test driver for Frame/Grid program '''

X_COORD = 0
Y_COORD = 0
BOX_WIDTH = 10
BOX_HEIGHT = 10

def main():
    # Create a new wx python app 
    app = wx.App()

    # Create the sample Frame
    frame = wx.Frame(None, -1, 'TestFrame.py')

    # Testing Grid
    grid = Grid(32,31)
    grid.setValue(0,0,1)
    grid.setValue(23,18,1)
    grid.setValue(5,5,1)
    grid.setValue(2,5,1)
    grid.setValue(4,8,1)
    grid.setValue(2,2,1)

    # Create the colored grid
    box = Box(frame,-1,grid)
    box.Draw(grid,X_COORD,Y_COORD,BOX_WIDTH,BOX_HEIGHT)

    # Display the sample frame
    frame.Show(True)
    app.MainLoop();

# Start
if __name__ == '__main__':
	main()


