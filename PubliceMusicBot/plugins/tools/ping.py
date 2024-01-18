from PubliceMusicBot.core.call import PubliceMusic
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PubliceMusicBot.utils.database import get_served_chats, get_served_users, get_sudoers
from PubliceMusicBot.core.userbot import assistants
from PubliceMusicBot import app
from PubliceMusicBot.utils import bot_sys_stats
from PubliceMusicBot.utils.decorators.language import language
from PubliceMusicBot.utils.inline import supp_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance  # Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://telegra.ph/file/37b57c6aaaa793bba055a.jpg"
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**")
    await asyncio.sleep(1)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ..**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**")
    await asyncio.sleep(2)
    await response.edit_caption("**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ....**")
    await asyncio.sleep(2)
    await response.edit_caption("**📡sʏsᴛᴇᴍ ᴅᴀᴛᴀ ᴀɴᴀʟʏsᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ !**")
    await asyncio.sleep(3)
    await response.edit_caption("**📩sᴇɴᴅɪɴɢ sʏsᴛᴇᴍ ᴀɴᴀʟʏsᴇᴅ ᴅᴀᴛᴀ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    start = datetime.now()
    pytgping = await PubliceMusic.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    resp = (datetime.now() - start).microseconds / 1000
    text = "🏓 𝖯𝗈𝗇𝗀 : {0}ᴍs\n\n{1} 𝖲𝗒𝗌𝗍𝖾𝗆 𝖲𝗍𝖺𝗍𝗌 :\n\n↬ 𝖴𝗉𝖳𝗂𝗆𝖾 : {2}\n↬ 𝖱𝖠𝖬 : {3}\n↬ 𝖢𝖯𝖴 : {4}\n↬ 𝖣𝗂𝗌𝗄 : {5}\n↬ 𝖯𝗒-𝖳𝗀𝖼𝖺𝗅𝗅𝗌 : {6}ᴍs\n↬ ꜱᴇʀᴠᴇʀ ᴄʜᴀᴛꜱ : {7}\n↬ ꜱᴇʀᴠᴇʀ ᴜꜱᴇʀꜱ : {8}\n↬ ᴀꜱꜱɪꜱ ɪᴅꜱ : {9}".format(resp, app.name, UP, RAM, CPU, DISK, pytgping, served_chats, served_users, len(assistants))
    carbon = await make_carbon(text)
    captions = "**ㅤ  🏓 ᴘɪɴɢ...ᴘᴏɴɢ...ᴘɪɴɢ✨\nㅤ  🎸 ᴅɪɴɢ...ᴅᴏɴɢ...ᴅɪɴɢ💞**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
        )
    await response.delete()
