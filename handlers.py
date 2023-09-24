
import math

BASE_ULR='https://framex-dev.wadrid.net/api/video/Falcon%20Heavy%20Test%20Flight%20(Hosted%20Webcast)-wbSwFU6tY1c/frame'
low = 0
heigh = 0
current = 0

def initBot(bot, lastFrame):
    
    def initData():
        """
        This function is in charge of initiating default values for the globar properties that
        control the bot's algorithm data.
        """
        global current
        global heigh
        global low
        low = 0
        heigh = lastFrame
        current = 0

    initData()


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        """
        Trigger: /start
        Sends first message to user
        """
        text = f"Hello! Please type in a number between 0-{heigh} to start"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
        bot.register_next_step_handler(sent_msg, set_current)


    @bot.message_handler(func=lambda m: True)
    def launch_question(message):
        """
         Trigger: any kind of text from the user
        """
        cleanMessage = message.text.lower()
        if (cleanMessage not in ['yes', 'no']):
            not_valid(message)
        else:
            NewMidPoint(cleanMessage == 'yes',message.chat.id)

    def set_current(message):
        """
         Follow up question from: send_welcome
         Sets our starting point (frame for first picture sent)
        """
        global current
       
        num = None

        if message.text.isdigit():
            num = int(message.text)
     
        if num and current >= 0 and current < heigh:
            send_photo(message.chat.id, current)
            current = num
        else:
            text = f"Wrong number, Please type in a number between 0-{heigh} to start"
            sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
            bot.register_next_step_handler(sent_msg, set_current)

    def send_photo(chatId,n, retry=False, finish=False):
        """
         This function is in charge of sending a new image to the user.
        """
        global BASE_ULR
        link = f'{BASE_ULR}/{n}/'
        try:
            sent_msg = bot.send_photo(chat_id=chatId, photo=link)
            if not finish:
                text = "Has the rocket launch yet?"
                sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")
        except:
            if retry:
                text = "Something went wrong, please try starting the bot again by typing '/start'"
                sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")
            else:
                text = "There was an error sending the picutre, let me try again"
                sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")
                send_photo(chatId,n, True)

    def not_valid(message):
        """
         Follow up from 'launch_question' whenever an answer from the user is 
         unknown (confused state)
        """
        text = "Unknown answer! If you want to start again type **/start** else please use 'yes' or 'no' answers"
        sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

    def finish(chatId, n):
        text = f"Found it! Rocket launched in frame {n}"
        sent_msg = bot.send_message(chatId, text, parse_mode="Markdown")
        send_photo(chatId, n, False, True)
        initData()

    def NewMidPoint(answer,chatId):
        global current
        global heigh
        global low
        if answer == True:
            heigh = current
        else:
            low = current

        newNum = int( math.floor( (low + heigh)/2 ) )
        errorDiff = heigh - low
        if errorDiff == 1:
            finish(chatId, current)
        else:
            current = newNum
            send_photo(chatId,newNum)