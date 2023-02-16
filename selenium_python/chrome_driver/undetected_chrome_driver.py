import undetected_chromedriver
from selenium.webdriver.common.by import By
import time

options=undetected_chromedriver.ChromeOptions()
options.add_argument('--headless')
try:
    driver=undetected_chromedriver.Chrome(options=options)
    driver.get('https://www.atbmarket.com/product/kapusta-1-gat')
    #time.sleep(5)
    price = driver.find_element(By.CSS_SELECTOR, '[class="product-price__top"]').text
    print(f'Цена: {price}')
    print(type(price))

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()