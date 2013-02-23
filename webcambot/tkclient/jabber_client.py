import time
import xmpp
from ..lib.cfg_file import config

class JabberClient:

    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.server=self.user.split("@")[1]

    def isConnected(self):
        if self.cl.connected:
            return True
        else:
            return False

    def connect(self):
        self.jid=xmpp.protocol.JID(self.user)
        self.cl=xmpp.Client(self.server,debug=[])
        if not self.cl.connect():
            return False
        if not self.cl.auth(self.jid.getNode(),self.password):
            return False
        self.cl.sendInitPresence()
        return True


    def sendMsg(self,msg):
        if not self.isConnected():
            self.cl.reconnectAndReauth()
        self.cl.send(xmpp.protocol.Message(to=config.get("bot_username"),body=msg,typ="chat"))
    
    def testConnection(self):
        self.cl.send(xmpp.protocol.Message(to=config.get("bot_username"),body="echo",typ="chat"))
                           

if __name__=="__main__":
    c=JabberClient()
    c.connect()
    print "connected"
    c.sendMsg("howdy")
 


