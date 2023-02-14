from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By

from selenium_python.chrome_driver.auth_data import tel, password
from selenium.webdriver.common.keys import Keys
import pickle

from time import sleep

#options
options  = webdriver.ChromeOptions()

#fake user-agent
useragent=UserAgent()
options.add_argument(f'user-agent={useragent.random}')

#service
serv=Service('/home/andrey/Python Projects/OOP-and-other/selenium_python/chrome_driver/chromedriver')

#driver
driver=webdriver.Chrome(
    options=options,
    service=serv
)

try:
    # driver.get(url='https://www.instagram.com/')
    # sleep(5)
    # username_input=driver.find_element('name','username')
    # username_input.clear()
    # username_input.send_keys(f'{tel}')
    # sleep(5)
    # password_input=driver.find_element('name','password')
    # password_input.clear()
    # password_input.send_keys(f'{password}')
    # sleep(5)
    # password_input.send_keys(Keys.ENTER)
    # sleep(5)
    # dont_save_button=driver.find_element(By.CSS_SELECTOR,'[class="_acan _acao _acas _aj1-"]').click()
    # sleep(10)
    #
    # #cookies
    # pickle.dump(driver.get_cookies(), open(f'{tel}_cookies','wb'))

    driver.get('https://www.instagram.com/')
    sleep(5)

    for cookie in pickle.load(open(f'{tel}_cookies','rb')):
        driver.add_cookie(cookie)

    sleep(5)
    driver.refresh()
    sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()