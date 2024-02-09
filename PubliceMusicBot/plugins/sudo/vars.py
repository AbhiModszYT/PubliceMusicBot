import asyncio

from pyrogram import filters

import config
from PubliceMusicBot import app
from PubliceMusicBot.misc import SUDOERS
from PubliceMusicBot.utils.formatters import convert_bytes

@app.on_message(filters.command(["v","config"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    up_r = f"<a href={config.UPSTREAM_REPO}>Repo</a>"
    up_b = config.UPSTREAM_BRANCH
    owners = config.OWNER_ID
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    api = config.API_ID
    hash = config.API_HASH
    DURATIONLIMIT = config.DURATION_LIMIT
    log = config.LOGGER_ID
    owner = config.OWNER_USERNAME
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    if not config.MONGO_DB_URI:
        mongo = "No"
    else:
        mongo = "Yes"
    if not config.BOT_TOKEN:
        bot = "No"
    else:
        bot = "Yes"
    if not config.STRING1:
        sesson = "No"
    else:
        sesson = "Yes"
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"

    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "No"
    else:
        sotify = "Yes"


    text = f"""MUSIC BOT CONFIG :
UPSTREAM_REPO : {up_r}
UPSTREAM_BRANCH = <code>{up_b}</code>
API ID : <code>{api}</code>
API HASH : <code>{hash}</code>
BOT TOKEN : <code>{bot}</code>
MONGO DB : <code>{mongo}</code>
Assis ID : <code>{sesson}</code>
OWNER USERNAME : @{owner}
LOG Group Id : <code>{log}</code>
AUTO_LEAVING_ASSISTANT : <code>{ass}</code>
ASSISTANT_LEAVE_TIME : <code>{auto_leave}</code> seconds
SPOTIFY_CLIENT_ID : <code>{sotify}</code>
SPOTIFY_CLIENT_SECRET : <code>{sotify}</code>
TG_AUDIO_FILESIZE_LIMIT : <code>{tg_aud}</code>
TG_VIDEO_FILESIZE_LIMIT : <code>{tg_vid}</code>
GIT TOKEN : <code>{token}</code>
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
