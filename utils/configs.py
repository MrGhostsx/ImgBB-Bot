import os
import time


class Var(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 12345))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")
    FORCE_JOIN_CHANNEL = "Tech_Shreyansh1"  # Your channel username without @

    # To record start time of bot
    BOT_START_TIME = time.time()

    # You Can Get An API Key From https://api.imgbb.com.
    API = os.environ.get("API", None)

    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    BOT_NAME = os.environ.get("BOT_NAME", "")

    START_PIC = "https://i.ibb.co/RG0hxmyc/Uploaded-6910445402.jpg"
    HELP_PIC = "https://i.ibb.co/7xN16XVm/Uploaded-6910445402.jpg"


class Tr(object):

    START_TEXT = """
👋 Hi ! {} Welcome To @SnapLinkMasterBot

**With This Bot You Can Hosts Your Images On imgbb.com **

You Can Send An Image As Forwarded Message From Any Chat/Channel Or Upload It As Photo Or File.
"""

    ABOUT_TEXT = """🤖 **My Name:** [SnapLink](t.me/SnapLinkMasterBot)

📝 **Language:** [Python 3](https://www.python.org)

📚 **Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)

📡 **Hosted On:** [Railway](railway.app)

👨‍💻 **Developer:** [Tech Shreyansh](t.me/Tech_Shreyansh29)

💡 **Source Code:** [Github](https://github.com/TechyShreyansh)

👥 **Support Group:** [Admin Help](https://t.me/Tech_Shreyansh2)

📢 **Updates Channel:** [Tech Shreyansh](https://t.me/Tech_Shreyansh)


❤ [Donate](https://www.paypal.me/techshreyansh29) [PayPal]
"""

    HELP_TEXT = """💡 Just Send Me Your Photo And I'll Upload it To You .  That's it

❤ Donate <code>techshreyansh@uboi</code> [UPI]
"""

    ERR_TEXT = "⚠️ API Not Found"

    ERRTOKEN_TEXT = "😶 The Access Token Provided Is Expired, Revoked, Malformed Or Invalid For Other Reasons. DM @Tech_Shreyansh29",

    WAIT = "💬 Please Wait !!"
