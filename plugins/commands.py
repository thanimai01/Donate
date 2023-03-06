from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from helper.ban import BanChek
from helper.motor_db import db
from helper.utils import not_subscribed
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.database import insert, getid
from variables import STAT_STICK, PICS, ADMIN, DELAY, LOG_CHANNEL
from plugins.logo_maker import generate_logo
import asyncio
import random
from helper.txt import kr

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)
           ],[
           InlineKeyboardButton("🔄 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 🔄", url=f"https://t.me/{client.username}?start=start")            
           ]]
           )
       )

@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
       kikked = await BanChek(bot, message)
       if kikked == 400:
           return
       insert(int(message.chat.id))
       await message.reply_chat_action("Typing")    
       m=await message.reply_sticker(STAT_STICK)
       await asyncio.sleep(DELAY)
       await m.delete()             
       await message.reply_photo(
           photo=random.choice(PICS),
           caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",               
           reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/Sarbudeen786')
               ],[
               InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/Thanimaibots'),
               InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/thanimaisupport')
               ],[
               InlineKeyboardButton(' Iɴʟɪɴᴇ 🔍 Sᴇᴀʀᴄʜ ', switch_inline_query_current_chat='')
               ],[
               InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
               InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
               ]]
               )
           )
       if not await db.is_user_exist(message.from_user.id):
          await db.add_user(message.from_user.id)
          await bot.send_message(LOG_CHANNEL, text=f"""<i>
<u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{message.from_user.id}</code>
○ DC : <code>{message.from_user.dc_id}</code>
○ First Name : <code>{message.from_user.first_name}<code>
○ UserName : @{message.from_user.username}

By = {bot. mention}</i>""")     


         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    await message.reply_text(
    text = f"""
🔎 <b><u>𝗬𝗢𝗨𝗥 𝗗𝗘𝗧𝗔𝗜𝗟𝗦</u>

๏ 𝗧𝗚 𝗜𝗗 : <code>{message.from_user.id}</code>
๏ 𝗗𝗖 : <code>{message.from_user.dc_id}</code>
๏ 𝗙𝗜𝗥𝗦𝗧 𝗡𝗔𝗠𝗘 : <code>{message.from_user.first_name}<code>
๏ 𝗨𝗦𝗘𝗥 𝗡𝗔𝗠𝗘 : @{message.from_user.username}
๏ 𝗧𝗚 𝗟𝗜𝗡𝗞 : <code>https://t.me/{message.from_user.username}</code>

Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Usɪɴɢ Mᴇ❣️</b> """, 
     reply_markup=InlineKeyboardMarkup( [[
         InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
         ],[
         InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
         InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
         ]]
         )
     )

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message): 
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
      ms = await message.reply_text("Geting All ids from database ...........")
      ids = getid()
      tot = len(ids)
      await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
      for id in ids:
        try:
     	   await message.reply_to_message.copy(id)
        except:
     	   pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(bot, message):    
    msg = await bot.send_message(chat_id=message.chat.id, text="<b>Processing ...</b>")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")


@Client.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logosq(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return
    try:
      text = message.text.replace("logosq","").replace("/","").replace("[ᗷETᗩ]","").strip().upper()
      
      if text == "":
        return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETA\n/logosq BETA")
  
      x = await message.reply_text("`🔍 Generating Logo For You...`")  
      logo = await generate_logo(text,True)
  
      if "telegra.ph" not in logo:
        return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")
        
      if "error" in logo:
        return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{logo}`")
        
      await x.edit("`🔄 Done Generated... Now Sending You`")
      
      logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
      
      await message.reply_photo(logo,caption="**🖼 Logo Generated By [ᗷETᗩ]**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    except FloodWait:
      pass
    except Exception as e:
      try:
        await x.delete()
      except:
        pass
      return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")

@Client.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logo(bot, message):
  kikked = await BanChek(bot, message)
  if kikked == 400:
      return
  try:
    text = message.text.replace("logo","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETAs\n/logosq MKN")

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://telegra.ph//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption="**🖼 Logo Generated By [ᗷETᗩ]**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")


@Client.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By [ᗷETᗩ]**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()






