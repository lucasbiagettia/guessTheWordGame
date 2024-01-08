from old.model import ModelSingleton
from old.similarity_analizer import word_similarity
import telebot

BOT_TOKEN = 'TOKEN'
DAY_WORD = "conejo"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    sign = message.text
    sim = word_similarity(sign, DAY_WORD)
    sim
    res = f"tu score es {sim}"
    bot.send_message(message.chat.id, res , parse_mode="Markdown")


bot.infinity_polling()
