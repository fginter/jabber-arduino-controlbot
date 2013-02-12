from jabberbot_local import JabberBot, botcmd
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
        return self.serialComm.sendMsg("h %d"%int(angle))

    @botcmd
    def l(self, mess, args):
        """Moves left, fine step."""
        return self.pan("pan",-15)

    @botcmd
    def ll(self, mess, args):
        """Moves left, medium step."""
        return self.pan("pan",-45)

    @botcmd
    def lll(self, mess, args):
        """Moves left, large step."""
        return self.pan("pan",-90)
    
    @botcmd
    def r(self, mess, args):
        """Moves right, fine step."""
        return self.pan("pan",+15)

    @botcmd
    def rr(self, mess, args):
        """Moves right, medium step."""
        return self.pan("pan",+45)

    @botcmd
    def rrr(self, mess, args):
        """Moves right, large step."""
        return self.pan("pan",+90)


    @botcmd
    def tilt(self, mess, angle):
        """Pans given angle. Negative down, positive up."""
        return self.serialComm.sendMsg("v %d"%int(-angle))

    @botcmd
    def u(self, mess, args):
        """Moves up, fine step."""
        return self.tilt("tilt",+15)

    @botcmd
    def uu(self, mess, args):
        """Moves up, fine step."""
        return self.tilt("tilt",+30)
    
    @botcmd
    def d(self, mess, args):
        """Moves up, fine step."""
        return self.tilt("tilt",-15)

    @botcmd
    def dd(self, mess, args):
        """Moves up, fine step."""
        return self.tilt("tilt",-30)


if __name__=="__main__":
    import config
    username = config.botUsername
    password = config.botPassword
    bot = WebcamBot(username,password)
    bot.serve_forever()
