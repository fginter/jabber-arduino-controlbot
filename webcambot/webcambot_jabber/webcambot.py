from ..lib.jabberbot_local import JabberBot, botcmd
import datetime
from serial_comm import SerialComm

class WebcamBot(JabberBot):

    def __init__(self,username,password):
        JabberBot.__init__(self,username,password,debug=False)
        self.serialComm=SerialComm()

    @botcmd
    def echo(self, mess, args):
        """Echoes the command verbatim."""
        print "DBG", args
        return "echo "+args

    @botcmd
    def pan(self, mess, angle):
        """Pans given angle. Negative left, positive right."""
        print "pan"
        return self.serialComm.sendAndWaitForReply("h %d"%int(angle))

    @botcmd
    def tilt(self, mess, angle):
        """Pans given angle. Negative down, positive up."""
        print "TILT"
        return self.serialComm.sendAndWaitForReply("v %d"%int(angle))

