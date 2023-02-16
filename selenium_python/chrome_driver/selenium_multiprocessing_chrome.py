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
#options.add_argument('--headless')

# service
serv = Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')

# driver
driver = webdriver.Chrome(
    options=options,
    service=serv
)

def get_data(url):
    try:
        #создаем объект браузера

        driver = webdriver.Chrome(
            options=options,
            service=serv
        )
        driver.get(url=url)
        sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
