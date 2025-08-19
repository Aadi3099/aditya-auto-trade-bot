import os
import time
import logging
from smartapi import SmartConnect
import telebot
import pyotp


API_KEY = os.getenv("ANGEL_API_KEY")
CLIENT_ID = os.getenv("ANGEL_CLIENT_ID")
PASSWORD = os.getenv("ANGEL_PASSWORD")
TOTP_SECRET = os.getenv("TOTP_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

logging.basicConfig(level=logging.INFO)

def angel_login():
    obj = SmartConnect(api_key=API_KEY)
    otp = pyotp.TOTP(TOTP_SECRET).now()
    data = obj.generateSession(CLIENT_ID, PASSWORD, otp)
    logging.info("Angel SmartAPI logged in ✅")
    return obj

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(TELEGRAM_CHAT_ID, "🤖 Aditya Auto Trade Bot is LIVE 🚀")

def send_trade_alert(symbol, direction, entry, sl, targets):
    msg = f"""
📢 *Trade Alert* – {symbol}
📈 Direction: {direction}
🎯 Entry: {entry}
🛑 Stop-Loss: {sl}
🎯 Targets: {', '.join(map(str, targets))}
⚡ Reply YES to execute
    """
    bot.send_message(TELEGRAM_CHAT_ID, msg, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text and m.text.upper() == "YES")
def execute_trade(message):
    bot.send_message(TELEGRAM_CHAT_ID, "✅ Trade confirmed! (Execution will be added next step)")

if __name__ == "__main__":
    logging.info("Starting Telegram bot…")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            logging.error(f"Bot crashed: {e}") 
            time.sleep(5)






