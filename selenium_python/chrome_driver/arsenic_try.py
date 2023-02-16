import asyncio
from arsenic import get_session, browsers, services
import time
import requests
from bs4 import BeautifulSoup

async def get_prices(url:str):

    service = services.Chromedriver(binary="./chromedriver")
    browser = browsers.Chrome()
    async with get_session(service, browser) as session:
        go_to_url= await session.get(url)
        price=session.get_element('[class="jsx-2be52a4b5bdfcc8a Price__value_title"]')
        print(f'Цена : {price}')
        # carrot_eko=await session.get("https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/")
        # onion_eko = await session.get("https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/")
        # price_1= await session.get_element('[class="jsx-2be52a4b5bdfcc8a Price__value_title"]')
        # result_1=await price_1.get_text()

        # price_2 = await session.get_element('[class="jsx-2be52a4b5bdfcc8a Price__value_title"]')
        # result_2 = await price_2.get_text()
        # print(f'Цена : {result}')
        # results=[result_1,result_2]
        # print(results)
async def main(urls:list):
    tasks=[]
    for url in urls:
        tasks.append(asyncio.create_task(get_prices(url)))
    for task in tasks:
        await task

urls=[
    "https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/",
    "https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/"
]


start=time.time()
asyncio.run(main(urls))
end=time.time()
print(f'На выполнение асинхронного кода ушло {end-start:.4f} c')
print('------------------------------------------------')
print()



def price_parcing_atb():
    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection':'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    class_ = 'jsx-2be52a4b5bdfcc8a Price__value_title'

    urls = [
        'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
        'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
        # 'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
        # 'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
        # 'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/'
    ]
    results=[]
    print()
    print('--------------------------------')
    print('Начинаем парсить как обычно с сайта атб...')


    for url in urls:
        headers = HEADERS
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, 'html.parser')
        price = soup.find(class_=class_).text
        results.append(price)

    print(results)



start = time.time()
price_parcing_atb()
finish = time.time()
print(f'Время выполнения обычного парсинга для атб: {finish - start:.4f} секунд')