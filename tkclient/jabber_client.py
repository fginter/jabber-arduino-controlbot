import time
import xmpp

class JabberClient:

    def __init__(self):
        self.user="filip.webcamctrl2@jabbim.cz"
        self.password="dixicekdixicek"
        self.server="jabbim.cz"

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
        print self.cl.send(xmpp.protocol.Message(to="filip.webcambot@jabbim.cz",body=msg,typ="chat"))

if __name__=="__main__":
    c=JabberClient()
    c.connect()
    print "connected"
    c.sendMsg("howdy")
 


