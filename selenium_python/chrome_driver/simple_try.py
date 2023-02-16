import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import page_status
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

class PriseParser:
    ATB_regular_divclass = '[class="product-price__top"]'
    EKO_regular_divclass = '[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    VARUS_special_divclass = '[class="sf-price__special"]'
    SILPO_regular_divclass = '[class="current-integer"]'

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.useragent = UserAgent()
        self.options.add_argument(f'user-agent={self.useragent.random}')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument('--headless')
        self.serv = Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')
        self.driver=webdriver.Chrome(options=self.options,service=self.serv)

    async def get_page(self,url):
        try:
            print('Открываем страницу...')
            page=self.driver.get(url)
            time.sleep(5)
            print('Страница закрылась!')
            # print('Getting item\'s price....')
            # price=self.driver.find_element(By.CSS_SELECTOR,div_class)
            # print(price.text)
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

    async def all_at_the_same_time(self):
        start=time.time()
        urls = [
            'https://www.atbmarket.com/product/kartopla-1-gat',
            'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
            'https://varus.ua/kartoplya-1-gatunok-vag',
            'https://shop.silpo.ua/product/kartoplia-bila-531296'
        ]
        task_atb=asyncio.create_task(self.get_page(urls[0]))
        task_eko = asyncio.create_task(self.get_page(urls[1]))
        task_varus = asyncio.create_task(self.get_page(urls[2]))
        task_silpo = asyncio.create_task(self.get_page(urls[3]))

        await task_atb
        await task_eko
        await task_varus
        await task_silpo
        end=time.time()

        print(f'Выполнение кода заняло: {end-start:.4f} c')

res=PriseParser()
asyncio.run(res.all_at_the_same_time())