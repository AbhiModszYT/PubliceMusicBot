import asyncio

from pyrogram import filters

import config
from PubliceMusicBot import app
from PubliceMusicBot.misc import SUDOERS
from PubliceMusicBot.utils.formatters import convert_bytes

@app.on_message(filters.command(["vars","var","config"]) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    owners = config.OWNER_ID
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    api = config.API_ID
    hash = config.API_HASH
    bot = config.BOT_TOKEN
    mongo = config.MONGO_DB_URI
    DURATIONLIMIT = config.DURATION_LIMIT
    log = config.LOGGER_ID
    owner = config.OWNER_USERNAME
    sesson = config.STRING_SESSION
    auto_leave = config.ASSISTANT_LEAVE_TIME
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
UPSTREAM_BRANCH = {up_b}
API ID : {api}
API HASH : {hash}
BOT TOKEN : {bot}
MONGO DB : {mongo}
Assis ID : {sesson}
Play Limit : {play}
OWNER USERNAME : @{owner}
LOG Group Id : {log}
GIT_TOKEN : {token}
AUTO_LEAVING_ASSISTANT : {ass}
ASSISTANT_LEAVE_TIME : {auto_leave} seconds
SPOTIFY_CLIENT_ID : {sotify}
SPOTIFY_CLIENT_SECRET : {sotify}
TG_AUDIO_FILESIZE_LIMIT : {tg_aud}
TG_VIDEO_FILESIZE_LIMIT : {tg_vid}
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
