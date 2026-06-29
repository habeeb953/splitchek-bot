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
    """Health check endpoint for Render to verify the service is running."""
    return "SplitChek bot is running!"


def build_webapp_markup():
    """
    Creates and returns an inline keyboard markup with a button to open the WebApp.

    Returns:
        InlineKeyboardMarkup: Markup with a single WebApp button.
    """
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "📱 Открыть SplitChek",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    """
    Handles the /start command.
    Sends a welcome message with a button to open the SplitChek WebApp.

    Args:
        message: Telegram message object containing chat info.
    """
    markup = build_webapp_markup()
    bot.send_message(
        message.chat.id,
        "Привет! Я SplitChek — помогаю делить расходы в группе.\n\nНажми кнопку ниже чтобы открыть приложение 👇",
        reply_markup=markup
    )


@bot.message_handler(commands=["help"])
def help(message):
    """
    Handles the /help command.
    Sends a list of all available bot commands.

    Args:
        message: Telegram message object containing chat info.
    """
    bot.send_message(message.chat.id,
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/help - список команд\n"
        "/app - открыть приложение\n"
    )


@bot.message_handler(commands=["app"])
def open_app(message):
    """
    Handles the /app command.
    Sends a message with a button to open the SplitChek WebApp.

    Args:
        message: Telegram message object containing chat info.
    """
    markup = build_webapp_markup()
    bot.send_message(message.chat.id, "Открываю приложение 👇", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def unknown(message):
    """
    Handles any unrecognized message or command.
    Prompts the user to use /start or /help.

    Args:
        message: Telegram message object containing chat info.
    """
    bot.send_message(message.chat.id, "Используй /start или /help")


def run_bot():
    """
    Starts the Telegram bot polling loop.
    Automatically restarts polling if an error occurs.
    """
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
