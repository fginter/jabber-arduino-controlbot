from webcambot.webcambot_jabber.webcambot import WebcamBot
from webcambot.lib.cfg_file import config

if __name__=="__main__":
    username = config.get("bot_username")
    password = config.get("bot_password")
    bot = WebcamBot(username,password)
    bot.serve_forever()
