import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "Mdisklinksenderamgbot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisklinksenderamgbot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
🤖 My Name: <a href='https://t.me/Mdisklinksenderamgbot'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/Xxxxxxxxxxxxxxx_x_xxxxxxxxxx_x'>Ravan Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/Xxxxxxxxxxxxxxx_x_xxxxxxxxxx_x'>Ravan bot</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Drishyam_2_Hindi_Movies</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Drishyam_2_Hindi_Movies</a></b>
"""
