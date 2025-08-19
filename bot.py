import os
from telegram.ext import ApplicationBuilder, CommandHandler

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("✅ Bot is running on Railway!")

if __name__ == "__main__":
    if not TELEGRAM_TOKEN:
        raise ValueError("⚠️ TELEGRAM_TOKEN not set in Railway env vars")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot started...")
    app.run_polling()
