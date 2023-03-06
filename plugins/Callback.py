from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio
from helper.txt import kr
from pyrogram.errors import QueryIdInvalid
from pyrogram. types import InlineQuery
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle

@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text=kr.HELP_TXT,       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton(' Tᴇʟᴇɢʀᴀᴘʜ ', callback_data='teleph'), 
                  InlineKeyboardButton(' 😝 Fᴜɴ  ', callback_data='fun'), 
                  InlineKeyboardButton(' Sᴛɪᴄᴋᴇʀ ID ', callback_data='sticker')
                  ],[
                  InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
                  ],[
                  InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
                  InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=kr.ABOUT_TXT.format(bot.mention,__version__),
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "devs")
                  ],[
                  InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
                  InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
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
   elif data == "devs":
         await msg.message.edit(
             text=kr.DEV_TXT,
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("⚡💔𝐋𝐨𝐧𝐞𝐥𝐲 King💔⚡", url="https://t.me/Sarbudeen786")
                  ],[
                  InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data="about"),
                  InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=kr.FUN_TXT,      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data="help"),
                 InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
                 ]]
                 )
             )
   elif data == "don":
         await msg.message.edit(
             text=kr.DON_TXT,
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton('Pᴀʏ 💰 Aᴍᴏᴜɴᴛ', url='https://t.me/Sarbudeen786'),
                     ],[
                     InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
                     InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
                     ]]
                     )
                 )

   elif data == "teleph":
         await msg.message.edit(
             text=kr.TELE_TXT,
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
                     ],[
                     InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "help"),
                     InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
                     ]]
                     )
                 )

   elif data == "sticker":
         await msg.message.edit(
             text=kr.STICKER_TXT,
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
                     ],[
                     InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "help"),
                     InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
                     ]]
                     )
                 )

   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass

@Client.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="Dᴏɴᴀᴛᴇ Pᴀʏᴍᴇɴᴛ Oʀ Hᴇʀᴏᴋ Aᴄᴄᴏᴜɴᴛ", description="Dᴏɴᴀᴛᴇ Oɴʟʏ Oɴᴇ Rᴜᴘᴇᴇ 🥲.",
    input_message_content=InputTextMessageContent(message_text=kr.DON_TXT),
    reply_markup=InlineKeyboardMarkup( [[ 
        InlineKeyboardButton("Dᴏɴᴀᴛᴇ 💳", url="https://upayi.ml/happysfx24@ybl/10"),
        ],[
        InlineKeyboardButton("🧛‍♂️ Aᴅᴍɪɴ", url="https://t.me/tamil_kid"), 
        InlineKeyboardButton("ʜᴇʀᴏᴋ ⚜️ Aᴄᴄᴏᴜɴᴛ ", url="https://t.me/Happy_Kid_sk")
        ]] 
    ),
    thumb_url="https://telegra.ph/file/3d7e72118de22df4f553f.jpg") )

    answer.append(InlineQueryResultArticle(title="I Nᴇᴇᴅ Pʀɪᴠᴀᴛᴇ Bᴏᴛs  ", description="Fɪʀsᴛ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ.",
    input_message_content=InputTextMessageContent(message_text=kr.PRI_TXT),
    reply_markup=InlineKeyboardMarkup( [[ 
        InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url="https://t.me/tamil_kid")
        ],[
        InlineKeyboardButton("Pᴀʏ 💰 ₹80", url="https://upayi.ml/happysfx24@ybl/80"), 
        InlineKeyboardButton("Pᴀʏ 💰 ₹160", url="https://upayi.ml/happysfx24@ybl/160")
        ]]
    ),
    thumb_url="https://telegra.ph/file/25c04a16291bd879f6184.jpg") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass
























