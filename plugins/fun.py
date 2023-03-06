from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from helper.utils import not_subscribed
from helper.ban import BanChek
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random


RUN_STRINGS = (
   "Oh.. insolence... same as before.... there is no change.... it is not the kiss that does not hold the course...!!!",
   "Allah... every... passion of the children...",
   "  I don't know how to write, sir....I don't know how to read....",
   "Don't be silent today... After today's fort...",
   "If you don't build a coal that doesn't stand on fire thinking that it's ash, it will burn.",
   "There is only one life.  Understand, there is no heaven, no hell, 'one life', he decides where and how he wants it",
   "What a bombastic explosion! Such a terrific reveal!!",
   "Go Away Stupid in the House of My Wife and Daughter You Won't See Me a Minute Off  The Today... don't come down..",
   "I can do that, can I do that", "Just because there is cream in the cream biscuit, there is no tiger in the tiger biscuit. Pani milk too, man...",
   "When you go to the ballpark when you are scared, you can go to the ballpark.  It's as you said.",
   "My Lord.... You won't allow me to be good, will you.", "Car engine out completely...",
   "Don't get bored!!", "Midnight  Did your father make bread and chicken....",
   "Oh, when you all fall in love, it's love.... When we all fall in love, it's wire...",
   "Oh God, please save me only...",
   "For her sake.  A waste of drunk toddy and wet rain....",
   "Where have you been all this time......",
   "You don't know much English...",
   "All the dreams like twinkle stars...",
   "My neighborhood  Muthappa give him a way",
   "Aliya, will you give me the dowry amount that I tied to you",
   "You are so tired", "I was waiting with tears in my eyes.",
   "Go away and leave your mouth. Shut your mouth bloody gramavasis.",
   "Go away.  .\ patto die with you.", "Because of you, Gunollya, the natives and those who leave Gunollya, why are they living so shamelessly, Red Banana.",
) 


IKKA_STRINGS = (
    "CAACAgUAAxkBAAIDUmIN8bqiD5DYQLjQzUwH7-1AsH0eAAJGBAAClj7wVxJlL3v8QuaoHgQ",
    "CAACAgUAAxkBAAIDVmIN8cCiVJZl05m0wiggUJaOvYarAAL5BAACo7lRVClze9Et3bCJHgQ",
    "CAACAgUAAxkBAAIDV2IN8cSKz20_0T-f7BlHVQfQYPu_AAKfAwACA4rwV01BOgyNllX1HgQ",
    "CAACAgUAAxkBAAIDWGIN8coT1jTnXpetiFOKVGZVCX78AAJLBAACrXgAAVTcB_E8ndEu0h4E",
    "CAACAgUAAxkBAAIDWWIN8c-GSo6HX8bmIvJOwDXG1pJ-AAJkBAACbYZIVIF7psBskaRiHgQ",
    "CAACAgUAAxkBAAIDWmIN8dfwrILfwAABBczAR4DoYxpkvAACvwUAAlNOSFRraTuQ8L5Qzx4E",
    "CAACAgUAAxkBAAIDXGIN8eN4RRZPSvKW5OcDhBGnF_qIAAJtBQACwq0JVAnAmIgTMZr6HgQ",
    "CAACAgUAAxkBAAIDeGIN8ke0Qm7S8rWAp5XRHtG21RP1AAJzBQACg5tAVL8bVAS2wafYHgQ",
    "CAACAgUAAxkBAAIDfGIN8lvvH0C9VGSLMV7fvxJ9L_r9AAIlBgACf4hJVA_SXDgpTipeHgQ",
    "CAACAgUAAxkBAAIDf2IN8nL54y-xsW_PGMX5T96e_ErnAAJiAwACjh3YV6f4T7ZwQqExHgQ",
    "CAACAgUAAxkBAAIDgmIN8oZFf70SfKUOl9nnk0Q0uIGPAAJjAwAC3-lRVqPrbp8AAeUBch4E",
    "CAACAgUAAxkBAAIDj2IN86K_5xEpxc00sVRoFLgNgvh_AALeAgACh49oVh2VB0KUEX3zHgQ",
    "CAACAgUAAxkBAAIDkmIN87LWn-56jo9wHTdifHsdBCAiAAJPAwACK4yZVlCyU1tXbk2YHgQ",
) 


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

@Client.on_message(filters.command("dice"))
async def roll_dice(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎲")

@Client.on_message(filters.command("arrow"))                                      
async def roll_arrow(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎯")

@Client.on_message(filters.command("goal"))
async def roll_goal(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "⚽️")

@Client.on_message(filters.command("luck"))
async def roll_luck(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎰")

@Client.on_message(filters.command("throw"))
async def roll_throw(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🏀")

@Client.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    await bot.send_dice(message.chat.id, "🎳")


@Client.on_message(filters.command("runs") &
    f_onw_fliter
)
async def runs(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

@Client.on_message(filters.command("ikka") &
    f_onw_fliter
)
async def ikka(bot, message):
    kikked = await BanChek(bot, message)
    if kikked == 400:
        return 
    """ /ikka strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)


