from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_argument('user-agent=HelloWorld:)')

driver=webdriver.Chrome(
    executable_path='/home/andrey/Python Projects/OOP-and-other/selenium_python/firefox_driver/geckodriver',
    options=options
)
try:
    driver.get(url='https://www.whatismybrowser.com/detect/what-is-my-user-agent')
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()