import os

import telebot
from dotenv import load_dotenv
from handlers import *
from flask import Flask,request 

server = Flask(__name__)
load_dotenv()
    
BOT_TOKEN = os.environ.get('BOT_TOKEN')
APP_NAME = os.environ.get('APP_NAME')

def main():

    if BOT_TOKEN:
        bot = telebot.TeleBot(BOT_TOKEN)

        bot.remove_webhook()
        bot.set_webhook(url='https://rocket-launch-bot-48bd3338ef98.herokuapp.com/' + BOT_TOKEN)
        
        initBot(bot,61695)
        print("initiated bot")
        bot.infinity_polling()
    else:
        print('Error with BOT INIT')

@server.route("/")
def webhook():
    main()
    return "!", 200

@server.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))