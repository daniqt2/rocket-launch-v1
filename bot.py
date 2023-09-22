import os
import math

import telebot
from fetchInfo import get_image

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

low = 0
heigh = 60000
current = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Hello! Please type in a number to start"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, set_current)


def num_handler(message):
    print(message.text)
    num = message.text
    bot.reply_to(message, "Has the rocket launched yet ? ")

# @bot.message_handler(commands=['yes'])
# def echo_all(message):
#     sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(sent_msg, day_handler)

# @bot.message_handler(commands=['no'])
# def echo_all(message):
#     sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(sent_msg, day_handler)

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = "Type rocket to start with the images"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)


@bot.message_handler(func=lambda m: True)
def launch_question(message):
    print(message.text == 'yes',message.text == 'no' )
    sign = message.text
    lol(message.text == 'yes',message.chat.id)

def set_current(message):
    global current
    current = message.text
    send_photo(message.chat.id, current)

def send_photo(chatId,n):
    print("!!!!!!!!", n)
    link = f'https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame/{n}/'
    sent_msg = bot.send_photo(chat_id=chatId, photo=link)
    text = "Has the rocket launch yet?"
    sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")

def finish(chatId, n):
    text = f"Found it! Rocket launched in frame {n}"
    sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")

def lol(answer,chatId):
    global current
    global heigh
    global low
    if answer == True:
        heigh = int(current) 
    else:
        low = int(current) 
   
    
    newNum = int( math.floor( (low + heigh)/2 ) )
    if newNum == current:
        finish(chatId, current)
    else:
        current = newNum
        print("------------------------")
        print("new", heigh, low , "CURRENT:",newNum)
        send_photo(chatId,newNum)

bot.infinity_polling()