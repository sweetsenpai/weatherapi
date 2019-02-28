import requests
from pprint import pprint
import re
from bs4 import BeautifulSoup as bs


def weather(town):
    city = town
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ff4138355d772de3d5e02734eea46925'.format(city)

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65'
    }
    session = requests.Session()
    ask = session.get(url, headers=headers)
    if ask.status_code == 404:
        return ('Возникли какие-то проблемы😱,\nпроверти правильно ли вы ввели название вашего города.\n'
                'Если все верно,пожалуйста введите название вашего города латинецей.')
    res = requests.get(url)
    data = res.json()
    #print(data)
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    degrees = int(temp - 273.15)
    description = data['weather'][0]['description']
    if degrees <= 0:
        a =('Температура : ' + str(degrees) + '°' + "❄\n")
    elif degrees < 10:
        a = ('Температура : ' + str(degrees) + '°' + ' 👌\n')
    elif degrees > 10:
        a = ('Температура : ' + str(degrees) + '°' + '☀\n')
    a = a + ('Скорость ветра 🌬️: {} м/с'.format(wind_speed))
    return a
