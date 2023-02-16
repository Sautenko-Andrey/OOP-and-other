import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import page_status
from time import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

async def pool_data(url,div_class):
    print('Создание браузера....')
    # options
    options = webdriver.ChromeOptions()

    # fake user-agent
    useragent = UserAgent()
    options.add_argument(f'user-agent={useragent.random}')

    # чтобы сайт не распознавал,что мы под ним заходим. Для маскировки под обычный браузер.
    options.add_argument('--disable-blink-features=AutomationControlled')

    # для запуска сайта в фоновом режиме
    options.add_argument('--headless')

    # service
    serv = Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')

    # driver
    driver = webdriver.Chrome(
        options=options,
        service=serv
    )
    print('Подключение к сайтам магазинов.....')
    driver.get(url)
    print('Забираем информацию о цене....')
    res=driver.find_element(By.CSS_SELECTOR, f'[class={div_class}]')
    return res

async def get_price():

    ATB_regular_divclass='product-price__top'
    EKO_regular_divclass='jsx-2be52a4b5bdfcc8a Price__value_title'
    VARUS_special_divclass='sf-price__special'
    SILPO_regular_divclass='current-integer'

    urls=[
        'https://www.atbmarket.com/product/kartopla-1-gat',
        'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
        'https://varus.ua/kartoplya-1-gatunok-vag',
        'https://shop.silpo.ua/product/kartoplia-bila-531296'
    ]

    atb_result=await pool_data(urls[0],ATB_regular_divclass)
    eko_result = await pool_data(urls[1], EKO_regular_divclass)
    varus_result = await pool_data(urls[2], VARUS_special_divclass)
    silpo_result = await pool_data(urls[3], SILPO_regular_divclass)

    result=[atb_result, eko_result,varus_result,silpo_result]
    print('Получаем результат....')
    print(result)


asyncio.run(get_price())








