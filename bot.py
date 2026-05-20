import telebot
import os
import threading
from flask import Flask

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@app.route('/')
def home():
    return "SplitChek bot is running!"


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я SplitChek бот. Используй /help чтобы увидеть команды.")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/help - список команд\n"
        "/balance - проверить баланс\n"
        "/expenses - список расходов\n"
    )


@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.send_message(message.chat.id, "Я не понимаю эту команду. Напиши /help чтобы увидеть список команд.")


def run_bot():
    bot.polling()


if __name__ == "__main__":
    thread = threading.Thread(target=run_bot)
    thread.daemon = True
    thread.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
