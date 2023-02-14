from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from random import choice
from fake_useragent import UserAgent

useragent=UserAgent()

user_agents_list=[
    'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
]

options=webdriver.ChromeOptions()
# options.add_argument('user-agent=Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
s=Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')
#options.add_argument(f'user-agent={choice(user_agents_list)}')
options.add_argument(f'user-agent={useragent.random}')
#options.add_argument('--proxy-server=138.128.65:8000')

driver=webdriver.Chrome(
    service=s,
    options=options
)
try:
    # driver.get(url='https://www.atbmarket.com/product/kapusta-1-gat')
    # time.sleep(5)

    driver.get(url='https://www.atbmarket.com/product/kapusta-1-gat')
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()