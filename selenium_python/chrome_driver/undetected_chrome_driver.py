import undetected_chromedriver
from selenium.webdriver.common.by import By
import time

options=undetected_chromedriver.ChromeOptions()
options.add_argument('--headless')
try:
    driver=undetected_chromedriver.Chrome(options=options)
    driver.get('https://novus.online/product/kartopla-rozeva-vag')
    price = driver.find_element(By.CSS_SELECTOR, '[class="product-card__price-current h4"]').text
    time.sleep(5)

    print(f'Цена : {price}')


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()