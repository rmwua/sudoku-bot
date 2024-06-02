from telebot.types import Message
from loader import bot


@bot.message_handler(func=lambda message: True)
def reply_hello(message):
    if message.text.lower() == "Привет":
        bot.send_message(message.chat.id, "Приветствую! Я бот. Пока что нахожусь в разработке.")