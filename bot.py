import telebot

TOKEN = "8569307483:AAHdxagIvoT5ASblm-udIX43Igbb7YbpV7E"

telebot.apihelper.proxy = {
    'http': 'http://80.71.232.86:443',
    'https': 'http://80.71.232.86:443'
}

bot = telebot.TeleBot(TOKEN)


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


bot.polling()