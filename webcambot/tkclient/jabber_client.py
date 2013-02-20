import time
import xmpp
from ..lib.cfg_file import config

class JabberClient:

    def __init__(self):
        self.user=config.get("tkclient_username")
        self.password=config.get("tkclient_password")
        self.server=self.user.split("@")[1]

    def connect(self):
        self.jid=xmpp.protocol.JID(self.user)
        self.cl=xmpp.Client(self.server,debug=[])
        self.cl.connect()
        print "conn"
        self.cl.auth(self.jid.getNode(),self.password)
        print "auth"
        self.cl.sendInitPresence()

    def sendMsg(self,msg):
#        if not self.cl.connected():
#            self.cl.reconnectAndReauth()
        self.cl.send(xmpp.protocol.Message(to=config.get("bot_username"),body=msg,typ="chat"))
    
    def testConnection(self):
        self.cl.send(xmpp.protocol.Message(to=config.get("bot_username"),body="echo",typ="chat"))
                           

if __name__=="__main__":
    c=JabberClient()
    c.connect()
    print "connected"
    c.sendMsg("howdy")
 


