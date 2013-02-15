from ..lib import appdirs
from Tkinter import *
from arrow_pad import ArrowPad		
from jabber_client import JabberClient

class App:

	def __init__(self,parent):
		self.f = Frame(parent)
		self.arrPad=ArrowPad(self.f,self.controlButtonPress)
		self.arrPad.pack()
		self.f.pack()

		self.jabberClient=JabberClient()
		self.jabberClient.connect()
		
	def controlButtonPress(self,bName):
		self.jabberClient.sendMsg(bName)
