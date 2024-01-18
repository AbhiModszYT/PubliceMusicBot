from PubliceMusicBot.core.bot import PubliceMusic
from PubliceMusicBot.core.dir import dirr
from PubliceMusicBot.core.git import git
from PubliceMusicBot.core.userbot import Userbot
from PubliceMusicBot.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PubliceMusic()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
