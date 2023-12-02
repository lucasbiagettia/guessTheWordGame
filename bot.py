import telebot

BOT_TOKEN = '6794189393:AAE6ZzH2wriksGIv7lvnwOi7odaKcjrZtB0'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    sign = message.text
    print(sign)
    bot.send_message(message.chat.id, 'hola', parse_mode="Markdown")


bot.infinity_polling()
