from Tkinter import *
from ..lib.cfg_file import config

class OptionsWindow (Toplevel):

    def __init__(self,*args,**kwargs):
        Toplevel.__init__(self,*args,**kwargs)
        self.title("Options")

        self.connFrame=LabelFrame(self)
        
        Label(self.connFrame,text="Username").grid(row=0,column=0,sticky=W)
        self.userNameE=Entry(self.connFrame)
        self.userNameE.grid(row=0,column=1)
        Label(self.connFrame,text="Password").grid(row=1,column=0,sticky=W)
        self.passwordE=Entry(self.connFrame)
        self.passwordE.grid(row=1,column=1)
        Label(self.connFrame,text="Bot address").grid(row=2,column=0,sticky=W)
        self.botAddressE=Entry(self.connFrame)
        self.botAddressE.grid(row=2,column=1)
        Label(self.connFrame,text="Bot password").grid(row=3,column=0,sticky=W)
        self.botPasswordE=Entry(self.connFrame)
        self.botPasswordE.grid(row=3,column=1)
        self.connFrame.pack()

        self.angleFrame=LabelFrame(self)
        Label(self.angleFrame,text="Pan").grid(row=4,column=0,sticky=W)
        self.panFrame=Frame(self.angleFrame)
        self.pan1=Spinbox(self.panFrame,from_=5,to=90,increment=5,width=2)
        self.pan1.pack(side=LEFT)
        self.pan2=Spinbox(self.panFrame,from_=5,to=90,increment=5,width=2)
        self.pan2.pack(side=LEFT)
        self.pan3=Spinbox(self.panFrame,from_=5,to=90,increment=5,width=2)
        self.pan3.pack(side=LEFT)
        self.panFrame.grid(row=4,column=1,sticky=W)

        Label(self.angleFrame,text="Tilt").grid(row=5,column=0,sticky=W)
        self.tiltFrame=Frame(self.angleFrame)
        self.tilt1=Spinbox(self.tiltFrame,from_=5,to=45,increment=5,width=2)
        self.tilt1.pack(side=LEFT)
        self.tilt2=Spinbox(self.tiltFrame,from_=5,to=45,increment=5,width=2)
        self.tilt2.pack(side=LEFT)
        self.tiltFrame.grid(row=5,column=1,sticky=W)
        self.angleFrame.pack(pady=5)

        self.buttonFrame=Frame(self)
        self.saveB=Button(self.buttonFrame,text="Save",command=self.save)
        self.saveB.pack(side=LEFT)
        self.cancelB=Button(self.buttonFrame,text="Cancel",command=self.cancel)
        self.cancelB.pack(side=LEFT,padx=10)
        self.buttonFrame.pack(pady=5)

        self.readFromConfig()
        
    def fillTextFromConfig(self,entryField,key):
        entryField.delete(0,END)
        v=config.get(key)
        if v!=None:
            entryField.insert(0,v)

    def saveTextToConfig(self,entryField,key):
        v=entryField.get()
        if v:
            config.set(key,v)


    def readFromConfig(self):
        self.fillTextFromConfig(self.userNameE,"tkclient_username")
        self.fillTextFromConfig(self.passwordE,"tkclient_password")
        self.fillTextFromConfig(self.botAddressE,"bot_username")
        self.fillTextFromConfig(self.botPasswordE,"bot_password")
        self.fillTextFromConfig(self.pan1,"tkclient_pan1")
        self.fillTextFromConfig(self.pan2,"tkclient_pan2")
        self.fillTextFromConfig(self.pan3,"tkclient_pan3")
        self.fillTextFromConfig(self.tilt1,"tkclient_tilt1")
        self.fillTextFromConfig(self.tilt2,"tkclient_tilt2")

    def save(self):
        self.saveTextToConfig(self.userNameE,"tkclient_username")
        self.saveTextToConfig(self.passwordE,"tkclient_password")
        self.saveTextToConfig(self.botAddressE,"bot_username")
        self.saveTextToConfig(self.botPasswordE,"bot_password")
        self.saveTextToConfig(self.pan1,"tkclient_pan1")
        self.saveTextToConfig(self.pan2,"tkclient_pan2")
        self.saveTextToConfig(self.pan3,"tkclient_pan3")
        self.saveTextToConfig(self.tilt1,"tkclient_tilt1")
        self.saveTextToConfig(self.tilt2,"tkclient_tilt2")
        config.write()
        self.destroy()
    
    def cancel(self):
        self.destroy()
