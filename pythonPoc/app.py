from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Token del bot de Telegram
token = '6794189393:AAFRPg4nlC29DkgUGkpok2di7JujPyKGyCo'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

# Manejar el comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hola")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Manejar cualquier mensaje de texto
def handle_text(update, context):
    # Obtener el texto del mensaje
    texto = update.message.text


    # Hacer algo con el texto recibido
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Mensaje recibido: {texto}")

text_handler = MessageHandler(Filters.text & ~Filters.command, handle_text)
dispatcher.add_handler(text_handler)

# Iniciar el bot
updater.start_polling()
updater.idle()
