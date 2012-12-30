from jabberbot import JabberBot, botcmd
import datetime

class SystemInfoJabberBot(JabberBot):

    @botcmd
    def echo(self, mess, args):
        """Echoes the command verbatim."""
        return "echo "+args

    @botcmd
    def l(self, mess, args):
        """Moves left, fine step."""
        #Arduino comm goes here
        return "OK"

if __name__=="__main__":
    import config
    username = config.botUsername
    password = config.botPassword
    bot = SystemInfoJabberBot(username,password)
    bot.serve_forever()
