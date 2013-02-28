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
		if self.checkConfig():
			self.connect()
		else:
			self.jabberClient=None
			OptionsWindow(self.f)
			if self.checkConfig():
				self.connect()
		#self.f.after(1000,self.checkConnectionStatus)
	
	def connect(self):
		self.jabberClient=JabberClient(config.get("tkclient_username"),config.get("tkclient_password"))
		self.jabberClient.connect()
		self.signalConnectionStatus()
	
	def checkConfig(self):
		"""Checks whether username, password and bot address are present in the config"""
		return config.get("tkclient_username") and config.get("tkclient_password") and config.get("bot_username")

	def optionsButtonPress(self):
		o=OptionsWindow(self.f)

	def checkConnectionStatus(self):
		print "status check"
		self.f.after(1000, self.checkConnectionStatus)

	def signalConnectionStatus(self):
		if not self.jabberClient or not self.jabberClient.isConnected():
			self.arrPad.setSignal("connected","alert")
			return
		if self.jabberClient.isConnected():
			self.arrPad.setSignal("connected","ok")
		

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
