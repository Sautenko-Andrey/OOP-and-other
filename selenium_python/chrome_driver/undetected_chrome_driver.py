import undetected_chromedriver
from selenium.webdriver.common.by import By
import time

options=undetected_chromedriver.ChromeOptions()
options.add_argument('--headless')
try:
    driver=undetected_chromedriver.Chrome(options=options)
    driver.get('https://shop.nashkraj.ua/kovel/product/494322-kava-aroma-gold-70g-natur-rozch-subl-gran')
    price = driver.find_element(By.CSS_SELECTOR, '[class="nice_price"]').text
    time.sleep(5)
    price = price[:5]
    try:
        price=float(price.replace(',','.'))
    except Exception as ex:
        print('Короткая цена!')
        price=float(price[:2])



    print(price, type(price))


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()