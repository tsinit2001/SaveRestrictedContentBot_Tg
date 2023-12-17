#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29087479
API_HASH = 'c17b3ffa426f9cdb4e07874d0e8642dc'
BOT_TOKEN = '6638113583:AAEFfhTSg0OipYlEttvYe4fjbbzuSIu_TgU'
SESSION = 'BQBVQUhAgOT1MPTkv8Xu4XYiHBLFrxR08_L-sK1nkYVLWSLc42LYdolZJjTb_rSLh97GbjwuHkZtfYs9NpeSec0BkCnqULCmBXqA5ZWgaO6FmN-x_xMMzovvRfB7YpqXf2Q6filqD8zEbSkO5WNKWw38j29vfiBfZuuUO9ikvQiYsc1OvVSXHHgWespLxieRLm9MBLj8yvKSicyrCHOB72qaDx7D0fYiXTWu8Gq3CcQ9Tv13lZ3SMJ-p-78dFBE8gfksfR_6ohVrFXdd0o74sO1yvru9dl-gk7_KV5kWbSB06VTM-dqwVvYDbR6SIQzXR-IrQtncFRaaPGasK5Uwo8ndAAAAAXE0FzUA'
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
