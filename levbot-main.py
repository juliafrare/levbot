from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
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

def start_bot():
    global updater
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://levbot-bot.herokuapp.com/' + TOKEN)
    updater.idle()

start_bot()