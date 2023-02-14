from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

from time import sleep

#options
options  = webdriver.ChromeOptions()

#fake user-agent
useragent=UserAgent()
options.add_argument(f'user-agent={useragent.random}')

#service
serv=Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')

#отключение режима Web Driver чтобы сайты не определяли,что мы заходим под ним.Это полезно для парсинга

#для старого Chrome Driver до версии 79.0.3945.16
# options.add_experimental_option('excludeSwitches',['enable-automation'])
# options.add_experimental_option('useAutomationExtension', False)

#для нового Chrome Driver 79.0.3945.16 и новее отключаем режим веб дравйвера,
# чтобы сайт не распознавал,что мы под ним заходим. Для маскировки под обычный браузер.
options.add_argument('--disable-blink-features=AutomationControlled')

#driver
driver=webdriver.Chrome(
    options=options,
    service=serv
)

try:
    #тест на то,что сайт обнаружит наш вебрайвер
    driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()