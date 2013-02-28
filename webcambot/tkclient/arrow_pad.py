"""
This widget provides the arrow pad for navigating the camera.
"""

from Tkinter import *

class ArrowPad(Canvas):

    def __init__(self,master,buttonPressCallback=None):
        Canvas.__init__(self,master,height=125,width=175)
        self.recHandles={} #{TK handle:buttonName}
        self.leds={} #{led name : rectangle ID}
        self.leds["connected"]=self.create_rectangle(150,110,155,125)
        self.leds["remoteresponse"]=self.create_rectangle(160,110,165,125)
        self.setSignal("connected","alert")
        self.setSignal("remoteresponse","alert")
        self.buttonPressCallback=buttonPressCallback #This method is called with button name upon press
        self.bind("<Button-1>",self.mouseCallback)
        self.populateButtons()

    statusColors={"alert":"red","warning":"yellow","ok":"green"}
    def setSignal(self,signalName,status):
        self.itemconfig(self.leds[signalName],fill=ArrowPad.statusColors[status])
            

    def populateButtons(self):
        bPlacements={
			"pan 3":(3,0),
			"pan 2":(2,0),
			"pan 1":(1,0),
			"pan -1":(-1,0),
			"pan -2":(-2,0),
			"pan -3":(-3,0),
			"tilt -1":(0,-1),
			"tilt -2":(0,-2),
			"tilt 1":(0,1),
			"tilt 2":(0,2),
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
