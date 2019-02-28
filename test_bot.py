import time
import telebot
from telebot import apihelper
import money
#  from weatherapi import weather
apihelper.proxy = {'https': 'socks5://352354383:RiqvhK6t@phobos.public.opennetwork.cc:1090'}
TOKEN = "559015083:AAFmBW3TV6NEX579WlMEmgDczsuLekDxPIg"
bot = telebot.TeleBot(token=TOKEN)


"""
def findw(msg):
    # from a list of texts, it finds the one with the 'погода' sign
    for i in msg:
        if 'погода' in i:
            return i
"""


@bot.message_handler(commands=['start'])  # welcome message handler
def send_msg(message):
    bot.send_message(message.chat.id, 'Привет, это демонстративный бот,в нем ты найдешь реализацию различных функций,\n'
                                      'для того,что бы посмотреть что я умею напиши /help')


@bot.message_handler(commands=['help'])  # help message handler
def send_welcome(message):
    bot.send_message(message.chat.id, '/start\n/help\n/info\n/buttons')


@bot.message_handler(commands=['info'])
def send_msg(message):
    bot.send_message(message.chat.id, '😉\ncreated by: @Sweet_Sempai\n github: https://github.com/sweetsenpai')


@bot.message_handler(commands=['weather☁'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Функция на доработке')


@bot.message_handler(commands=['buttons'])
def buttons_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/help', '/info')
    user_markup.row('/weather☁', '/news📰', '/money💰')
    bot.send_message(message.chat.id, "Лови кнопки приятель⚙️", reply_markup=user_markup)

"""
@bot.message_handler(func=lambda msg: msg.text is not None and 'погода' or 'Погода' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def find_city(message):
    texts = message.text.split()
    at_text = findw(texts)
    bot.reply_to(message, weather(texts[-1]))
"""


@bot.message_handler(commands=['money💰'])
def get_money(message):
    bot.send_message(message.chat.id, money.money_status())


@bot.message_handler(commands=['news📰'])
def inline(message):
    key = telebot.types.InlineKeyboardMarkup(True,)
    but_1 = telebot.types.InlineKeyboardButton(text='Медуза', url='https://meduza.io')
    but_2 = telebot.types.InlineKeyboardButton(text='МедиаЗона', url='https://zona.media')
    but_3 = telebot.types.InlineKeyboardButton(text='Лента.ру', url='https://lenta.ru')
    key.row(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "НОВОСТИ", reply_markup=key)



while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)