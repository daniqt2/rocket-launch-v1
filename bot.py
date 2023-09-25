import os

import telebot
from dotenv import load_dotenv
from handlers import *
from flask import Flask

server = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot('6694134640:AAHeUhU9p3RXXJUzkYrbwBH2CNAFoDRJvGw')

def main():
    load_dotenv()

    if BOT_TOKEN:
        port = os.getenv('PORT', default=8000)
        updater.start_webhook(port=port)
        
        initBot(bot,61695)
        print("initiated bot")
        bot.infinity_polling()
    else:
        print('Error with BOT INIT')

@server.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    print(BOT_TOKEN)
    bot.set_webhook(url='https://rocket-launch-bot-48bd3338ef98.herokuapp.com/.herokuapp.com/' + BOT_TOKEN)
    return "!", 200


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    server.run(debug=True, host='0.0.0.0', port=port)
    main()