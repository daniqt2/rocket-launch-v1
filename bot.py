import os
from flask import Flask, request, Response

import telebot
from dotenv import load_dotenv
from handlers import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    load_dotenv()
    print(os.environ.get('BOT_TOKEN'))

    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN:
        bot = telebot.TeleBot(BOT_TOKEN)

        initBot(bot,61695)

        bot.infinity_polling()
    else:
        print('Error with BOT INIT')
    if request.method == 'POST':

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)