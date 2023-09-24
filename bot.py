import os


import telebot
from dotenv import load_dotenv
from handlers import *


def main():
    load_dotenv()
    print(os.environ.get('BOT_TOKEN'))

    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN:
        bot = telebot.TeleBot(BOT_TOKEN)
        
        initBot(bot,61695)
        
        bot.infinity_polling()
    else:
        print('Error with BOT INIT')


if __name__ == '__main__':
    main()