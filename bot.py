import os
from telegram.ext import Updater, CommandHandler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
    update.message.reply_text("✅ Bot is running on Railway!")

if __name__ == "__main__":
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
