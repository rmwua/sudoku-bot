from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["helloworld"])
def bot_hello(message: Message):
    bot.reply_to(message, "Hello World!")


