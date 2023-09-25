import os

import telebot
from dotenv import load_dotenv
from handlers import *
import flask

app = flask.Flask(__name__)

WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PORT = os.environ.get('PORT') 
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

def main():
    load_dotenv()

    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN:
        bot = telebot.TeleBot(BOT_TOKEN)

        bot.remove_webhook()
        
        initBot(bot,61695)
        print("initiated bot")
        bot.infinity_polling()
    else:
        print('Error with BOT INIT')

@app.route('/', methods=['GET', 'HEAD'])
def index():
    main()
    return ''
    

# Start flask server
app.run(host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        debug=True)