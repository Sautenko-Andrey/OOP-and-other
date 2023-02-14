import time

import requests
from selenium import webdriver

def get_data(url):
    headers = {
        "Accept": '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }

    r=requests.get(url=url,headers=headers)

    with open('index.html','w') as file:
        file.write(r.text)


def get_data_with_selenium(url):
    options=webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0')

    try:
        driver=webdriver.Firefox(
            executable_path='/home/andrey/Python Projects/OOP-and-other/geckodriver',
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open('index_selenium.html', 'w') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    # get_data('https://shop.silpo.ua/product/mandaryn-ispaniia-142338')
    get_data_with_selenium('https://shop.silpo.ua/product/mandaryn-ispaniia-142338')


if __name__=='__main__':
    main()