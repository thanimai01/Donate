import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from telegraph import upload_file
from helper.utils import not_subscribed
from helper.ban import BanChek

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**⚠️Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)
           ],[
           InlineKeyboardButton("🔄 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 🔄", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.command(["tgmedia", "tgraph", "telegraph"]))
async def telegraph(client, message):
    kikked = await BanChek(client, message)
    if kikked == 400:
        return 
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return    
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    mkn=await message.reply_text(
        text="<code>Trying to processing please weit.....</code>",
        disable_web_page_preview=True
    )
    await asyncio.sleep(2)
    await mkn.delete()
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            text=f"<b>Link:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Oᴘᴇɴ 🔗 Lɪɴᴋ", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="Sʜᴀʀᴇ 🍂 Lɪɴᴋ", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
                ],
                [InlineKeyboardButton(text="✗ Cʟᴏsᴇ ✗", callback_data="close")]
            ]
        )
    )
    finally:
        os.remove(download_location)
