import telebot
import os
import threading
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
        "Привет! Я SplitChek — помогаю делить расходы в группе.\n\nНажми кнопку ниже чтобы открыть приложение ",
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
