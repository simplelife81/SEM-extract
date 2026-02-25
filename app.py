import os
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from cleanup import start_cleanup_scheduler

# start auto cleanup
start_cleanup_scheduler()

# ---------- Flask keep alive ----------
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running ✅"

def run_web():
    web.run(host="0.0.0.0", port=8080)

Thread(target=run_web).start()

# ---------- Telegram Bot ----------
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "bot_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        "✅ Bot deployed successfully!\n"
        "Your bot is working perfectly 🚀"
    )

async def main():
    await bot.start()
    print("Bot Started")
    await bot.idle()

if __name__ == "__main__":
    asyncio.run(main())
