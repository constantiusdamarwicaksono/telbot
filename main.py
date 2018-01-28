# python based telegram bot using python-telegram-bot
from time import sleep
from telegram.ext import Updater,MessageHandler,Filters
from util import get_token
import logging

def say_hello(bot,update)->None:
    logging.info("new message from : "+str(update.effective_user.first_name))
    bot.send_message(chat_id=update.message.chat_id, text="Hello i'am bot")

def main()->None:
    token = get_token()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    updater = Updater(token)
    try :
        updater.start_polling()
        updater.dispatcher.add_handler(MessageHandler(Filters.text,say_hello))
        #sleep(10)
        #updater.stop()
    except KeyboardInterrupt :
        updater.stop()

if __name__ == "__main__":
    main()
