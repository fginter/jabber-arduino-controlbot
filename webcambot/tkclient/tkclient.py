from ..lib import appdirs
from ..lib.cfg_file import config
from Tkinter import *
from arrow_pad import ArrowPad		
from jabber_client import JabberClient
from options_window import OptionsWindow

class App:

	def __init__(self,parent):
		self.parent=parent
		self.f = Frame(parent)
		self.arrPad=ArrowPad(self.f,self.controlButtonPress)
		self.arrPad.pack()
		self.optButton=Button(self.f,text="Options...",command=self.optionsButtonPress)
		self.optButton.pack()
		self.f.pack()

		#self.jabberClient=JabberClient()
		#self.jabberClient.connect()
	
	def optionsButtonPress(self):
		o=OptionsWindow()
		

	def controlButtonPress(self,bName): #bName is "pan|tilt [+-][123]"
		command,amount=bName.split()
		amount=int(amount)
		if amount<0:
			direction=-1
			amount=-amount
		else:
			direction=1
			amount=amount
		degrees=int(config.get("tkclient_%s%d"%(command,amount))) #Look up config file vars like tkclient_pan1
		self.jabberClient.sendMsg("%s %d"%(command,degrees*direction))
