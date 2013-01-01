from jabberbot import JabberBot, botcmd
import datetime

class WebcamBot(JabberBot):

    @botcmd
    def echo(self, mess, args):
        """Echoes the command verbatim."""
        return "echo "+args

    @botcmd
    def pan(self, mess, angle):
        """Pans given angle. Negative left, positive right."""
        #Arduino comm goes here
        return "OK"

    @botcmd
    def l(self, mess, args):
        """Moves left, fine step."""
        return self.pan("pan","-15")
    
    @botcmd
    def r(self, mess, args):
        """Moves right, fine step."""
        return self.pan("pan","+15")


    @botcmd
    def tilt(self, mess, angle):
        """Pans given angle. Negative down, positive up."""
        #Arduino comm goes here
        return "OK"

    @botcmd
    def u(self, mess, args):
        """Moves up, fine step."""
        return self.tilt("tilt","+15")
    
    @botcmd
    def r(self, mess, args):
        """Moves down, fine step."""
        return self.pan("tilt","-15")



if __name__=="__main__":
    import config
    username = config.botUsername
    password = config.botPassword
    bot = SystemInfoJabberBot(username,password)
    bot.serve_forever()
