import os
from telegram.ext import Updater, CommandHandler
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update, context):
	update.message.reply_text("✅ Bot is running on Railway!")

if __name__== "__main__":
	if not TELEGRAM_TOKEN:
		raise ValueError("⚠️ TELEGRAM_TOKEN is not set in environment ariables!")

	updater = Updater(TELEGRAM_TOKEN, use_context=True)
	dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
	
	print("🚀Bot started...")
	updater.start_polling()
	updater.idle()

