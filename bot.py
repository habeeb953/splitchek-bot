import telebot
import os
import threading
import time
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("ERROR: BOT_TOKEN environment variable is not set!")
    exit(1)

print(f"Token loaded: {TOKEN[:10]}...")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://splitchek-bot.onrender.com")


@app.route('/')
def home():
    return "SplitChek bot is running!"


@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        " Открыть SplitChek",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    bot.send_message(
        message.chat.id,
        "Привет! Я SplitChek — помогаю делить расходы в группе.\n\nНажми кнопку ниже чтобы открыть приложение 👇",
        reply_markup=markup
    )


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/help - список команд\n"
        "/app - открыть приложение\n"
    )


@bot.message_handler(commands=["app"])
def open_app(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        " Открыть SplitChek",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    bot.send_message(message.chat.id, "Открываю приложение ", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.send_message(message.chat.id, "Используй /start или /help")


def run_bot():
    while True:
        try:
            print("Starting bot polling...")
            bot.polling(non_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Bot polling error: {e}")
            time.sleep(5)
            print("Restarting polling...")


port = int(os.environ.get("PORT", 5000))

bot_thread = threading.Thread(target=run_bot)
bot_thread.daemon = True
bot_thread.start()

print(f"Starting Flask on port {port}...")
app.run(host="0.0.0.0", port=port)
