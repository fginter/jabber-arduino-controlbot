"""
This widget provides the arrow pad for navigating the camera.
"""

from Tkinter import *

class ArrowPad(Canvas):

    def __init__(self,master,buttonPressCallback=None):
        Canvas.__init__(self,master,height=125,width=175)
        self.recHandles={} #{TK handle:buttonName}
        self.buttonPressCallback=buttonPressCallback #This method is called with button name upon press
        self.bind("<Button-1>",self.mouseCallback)
        self.populateButtons()

    def populateButtons(self):
        bPlacements={
			"lll":(-3,0),
			"ll":(-2,0),
			"l":(-1,0),
			"r":(1,0),
			"rr":(2,0),
			"rrr":(3,0),
			"u":(0,-1),
			"uu":(0,-2),
			"d":(0,1),
			"dd":(0,2),
                        }
        
        for bName,(xG,yG) in bPlacements.iteritems():
            x=(xG+3)*25+2
            y=(yG+2)*25+2
            recHandle=self.create_rectangle(x, y, x+20, y+20, fill="blue",tags="but")
            self.recHandles[recHandle]=bName
        
    def mouseCallback(self,event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        buttonName=self.recHandles[canvas.find_closest(x, y)[0]]
        if self.buttonPressCallback!=None:
            self.buttonPressCallback(buttonName)


if __name__=="__main__":

    def cb(b):
        print b

    master = Tk()
    w = ArrowPad(master,cb)
    w.pack()
    mainloop()
