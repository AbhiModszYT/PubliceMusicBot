import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID","6435225")) # Get this value from my.telegram.org/apps
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d") # Get this value from my.telegram.org/apps
BOT_TOKEN = getenv("BOT_TOKEN") # Get your token from @BotFather on Telegram.
MONGO_DB_URI = getenv("MONGO_DB_URI", None) # Get your mongo url from cloud.mongodb.com
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001840241140"))  # Chat id of a group for logging bot's activities/ Music Play Logs
PUBLICELOGS = int(getenv("PUBLICELOGS", "-1001841879487")) # Chat id of a group for Bot Added Messege/Leaved Messege U can Add Your Support Group id Aslo
GBANLOGS = int(getenv("GBANLOGS", "-1001841879487")) #Add Here Your Gbans Logs Channel Id 
OWNER_ID = int(getenv("OWNER_ID", "5360305806")) # Get this value from @Sophia_x_MusicBot on Telegram by /id
OWNER = int(getenv("OWNER","5360305806"))
OWNER_USERNAME = getenv("OWNER_USERNAME","NEW_AMBOT")
## Fill these variables if you're deploying on heroku.
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")# Your heroku app name
HEROKU_API_KEY = getenv("HEROKU_API_KEY") # Get it from http://dashboard.heroku.com/account
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiModszYT/PubliceMusicBot")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)# Fill this variable if your upstream repository is private
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/+sKjT3eiF_jZjZjQ1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+sKjT3eiF_jZjZjQ1")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "900"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "900"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170") #Leave it
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc") #Leave it
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25)) #Leave it
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000")) #Leave it
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000")) #Leave it
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
AMBOT = [
    "💞",
    "🔎",
    "🔍",
    "🧪",
    "💣",
     "⚡️",
     "🔥",
     "🕺",
     "🎩",
     "🌈",
     "🍷",
     "🥂",
     "🍾",
    "🥃",
    "🥤",
    "🍽",
    "🍭",
    "🚗",
    "🚕",
    "🚓",
    "🚑",
    "🚀",
    "💎",
    "🔮",
    "🪄",
    "💌",
    "⁉️",
    "💤",
    "🧨"
]

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
clean = {}
lyrical = {}
LOG_FILE_NAME = "logs.txt"
LOG = 2
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = ["https://graph.org/file/04bc1c79ebdf6bbb15b05.jpg", 
                 "https://graph.org/file/d5da08b65b054e7183ae9.jpg", 
                 "https://graph.org/file/941558bfd46ee7f4c805b.jpg", 
                 "https://graph.org/file/4e07ecb0b1f68047fef51.jpg", 
                 "https://graph.org/file/2311d35739ca433f0b1c9.jpg", 
                 "https://graph.org/file/3ccbe5d1b2df1282afff8.jpg", 
                 "https://graph.org/file/13e35118f9db15f85d085.jpg"
                ]
PING_IMG_URL = getenv("PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL","https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
