import time
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5://352354383:RiqvhK6t@phobos.public.opennetwork.cc:1090'}
TOKEN = ""
bot = telebot.TeleBot(token=TOKEN)


def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i


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


@bot.message_handler(commands=['buttons'])
def buttons_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', '/help', '/info')
    user_markup.row('погода☁')
    bot.send_message(message.chat.id, "Лови кнопки приятель🔳", reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_msg(message):
    if message.text == 'погода☁':
        bot.send_message(message.chat.id, 'Совсем скоро эта функция будет добавлена😁')
    else:
        bot.send_message(message.chat.id, 'Я пока не знаю что с этим делать😢')


while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
