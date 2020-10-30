from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import Bot
from jpeg import moremorejpeg
import logging
import os

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)
updater = None

TOKEN = os.environ['TELEGRAM_TOKEN']

def start(update, context):
    s = "Bem vindo ao levbot!"
    update.message.reply_text(s)

def morejpeg(update, context):
    update.message.reply_text("Por favor, envie uma imagem.")

def get_photo(update, context):
    file_id = update.message.photo[-1].file_id
    file_content = context.bot.get_file(file_id)
    file_name = file_content.download()
    new_name = moremorejpeg(file_name)
    #update.message.reply_text(file_name)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=new_name)

def main():
    global updater
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('morejpeg', morejpeg))
    dispatcher.add_handler(MessageHandler(Filters.photo, get_photo))

    updater.start_polling()
    #updater.start_webhook(listen="0.0.0.0",
    #                      port=int(PORT),
    #                      url_path=TOKEN)
    #updater.bot.setWebhook('https://levbot-bot.herokuapp.com/' + TOKEN)
    updater.idle()

main()