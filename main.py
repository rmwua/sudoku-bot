import telebot
import secret

bot = telebot.TeleBot(secret.secret)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello world!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    # bot.send_message(message.chat.id, "Hello I am a bot")


if __name__ == "__main__":
    bot.infinity_polling()