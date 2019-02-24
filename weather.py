import requests
import re
from bs4 import BeautifulSoup as bs

headers ={
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.65'
}

base_url = 'https://www.google.ru/search?newwindow=1&client=opera&hs=M6D&biw=786&bih=970&ei=c8VuXPKaKaCLk74P76uSoA0&q=' \
           'погода+спб&oq=gjuj&gs_l=psy-ab.3.0.0i10i1i42j0i10i1l9.2732444.2733937..2735293...1.0..0.76.232.4......0....' \
           '1..gws-wiz.....6..0i71j35i39j0i131j0j0i10i1i67i42j0i10i1i67j0i67.W_PzLaifAp4'


def what_weather(base_url, headers):
    session = requests.Session()
    ask = session.get(base_url, headers=headers)
    if ask.status_code == 200:
        soup = bs(ask.content, 'html.parser')
        div = soup.find_all('div', attrs={'class': 'vk_c card-section', 'id': 'wob_wc'})
        for el in div:
            cel = el.find_all('span', attrs={'class': 'wob_t', 'id': 'wob_tm', 'style': 'display:inline'})
            num = str(cel)
        print(

        )
    else:
        print("We have some trouble")


what_weather(base_url, headers)
