from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

from selenium_python.chrome_driver.auth_data import tel, password
from selenium.webdriver.common.keys import Keys
import pickle

from time import sleep

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

try:
    print('Connecting to page.....')
    #driver.get('https://www.atbmarket.com/product/kapusta-1-gat')
    #driver.get('https://shop.silpo.ua/product/banan-32485')
    #driver.get('https://auchan.ua/sigarety-marlboro-20-sht-916786/')
    driver.get('https://www.tavriav.ua/product/70120/')
    sleep(1)
    print('Getting item\'s price....')
    #price=driver.find_element(By.CSS_SELECTOR,'[class="product-price__top"]')       # ATB
    #price = driver.find_element(By.CSS_SELECTOR, '[class="current-integer"]')        #Silpo
    #price = driver.find_element(By.CSS_SELECTOR, '[class="productDetails_price_actual__12u8E"]')   #Ashan
    price = driver.find_element(By.CSS_SELECTOR, '[class="product-info__price"]')   #tavria b
    print(price.text)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()