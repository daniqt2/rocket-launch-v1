import os

import telebot
from dotenv import load_dotenv
# from handlers import *

def main():
    load_dotenv()

    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN:
        bot = telebot.TeleBot(BOT_TOKEN)
        
        # initBot(bot,61695)
        print("initiated bot")
        bot.infinity_polling()
    else:
        print('Error with BOT INIT')


if __name__ == '__main__':
    main()