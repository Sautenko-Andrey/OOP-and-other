import asyncio
import aiohttp
from bs4 import BeautifulSoup
import requests
import time

async def get_page_data():
    """Это и есть задача.
    Парсер , который пробегается по каждой странице и записывает данные"""
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }

async def gather_data():
    '''Формирует необходимый список задач'''


    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
    }

    urls=[
        'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
        'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
        'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/',
        'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
        'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
    ]

    class_='jsx-161433026 Price__value_title'

    results=[]

    print('Начинаем парсить асинхронно...')
    start = time.time()

    #создаем клиент-сессию, которая позволяет повторно использовать уже открытое соединение.
    async with aiohttp.ClientSession() as session:
        for url in urls*3:
            response=await session.get(url=url,headers=HEADERS)
            soup=BeautifulSoup(await response.text(), 'html.parser')
            price = soup.find(class_=class_).text
            results.append(price)

        #print(results)

    finish = time.time()
    print(f'Время выполнения асинхронного парсинга: {finish - start:.4f} секунд')

asyncio.run(gather_data())


def price_parcing():
    HEADERS = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    class_ = 'jsx-161433026 Price__value_title'

    urls = [
        'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
        'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
        'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/',
        'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
        'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
    ]
    results=[]
    print()
    print('--------------------------------')
    print('Начинаем парсить как обычно...')
    start = time.time()

    for url in urls*3:
        headers = HEADERS
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        price = soup.find(class_=class_).text
        results.append(price)

    print(results)

    finish = time.time()
    print(f'Время выполнения обычного парсинга: {finish - start:.4f} секунд')

price_parcing()


def price_parcing_atb():
    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    class_ = 'product-price__top'

    urls = [
        'https://www.atbmarket.com/product/kapusta-1-gat'
    ]
    results=[]
    print()
    print('--------------------------------')
    print('Начинаем парсить как обычно с сайта атб...')
    start = time.time()

    for url in urls:
        headers = HEADERS
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        price = soup.find(class_=class_).find_next().text
        results.append(price)

    print(results)

    finish = time.time()
    print(f'Время выполнения обычного парсинга для атб: {finish - start:.4f} секунд')

price_parcing_atb()






