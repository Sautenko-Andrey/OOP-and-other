from bs4 import BeautifulSoup
import undetected_chromedriver
from selenium.webdriver.common.by import By


class ProductParserVol2:
    '''Класс для парсинга цен с сайтов с приминением Selenium'''

    SELECTOR = By.CSS_SELECTOR
    ATB_REGULAR_DIV_CLASS = '[class="product-price__top"]'
    EKO_REGULAR_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    EKO_DISCOUNT_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title Price__value_discount"]'
    VARUS_REGULAR_DIV_CLASS = '[class="sf-price__regular"]'
    VARUS_SPECIAL_DIV_CLASS = '[class="sf-price__special"]'
    VARUS_DISCOUNT_DIV_CLASS = '[class="jsx-161433026 Price__value_title Price__value_discount"]'


    def __init__(self):
        '''Инииализация драйвера Chrome со всеми нужными параметрами,
        а именно включение режима работы браузера в фоновом режиме'''
        self.options = undetected_chromedriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = undetected_chromedriver.Chrome(options=self.options)

    def prices_parsing(self, urls: list):
        results = ['out of stock','out of stock','out of stock']
        '''Парсинг цен для продукта сразу со всех досутпных маркетов.'''

        for url in urls:
            if url[:15] == 'https://www.atb':
                # парсим цену АТБ
                self.driver.get(url)
                try:
                    self.atb_price = self.driver.find_element(self.SELECTOR, self.ATB_REGULAR_DIV_CLASS).text

                    results[0]=self.atb_price
                    # if self.atb_price:
                    #     results.append(self.atb_price)
                    # else:
                    #     results.append('out of stock')
                except Exception as ex:
                    print(ex)

            elif url[:11] == 'https://eko':
                # парсим цену ЭКО
                self.driver.get(url)
                try:
                    self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_REGULAR_DIV_CLASS).text

                    results[1] = self.eko_price
                    # if self.eko_price:
                    #     results.append(self.eko_price)
                    # else:
                    #     results.append('out of stock')
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_DISCOUNT_DIV_CLASS).text

                            results[1] = self.eko_price
                            # if self.eko_price:
                            #     results.append(self.eko_price)
                            # else:
                            #     results.append('out of stock')
                        except Exception as ex:
                            print(ex)
            elif url[:13] == 'https://varus':
                # парсим цену Varus
                self.driver.get(url)
                try:
                    self.varus_price = self.driver.find_element(self.SELECTOR, self.VARUS_REGULAR_DIV_CLASS).text

                    results[2] = self.varus_price
                    # if self.varus_price:
                    #     results.append(self.varus_price)
                    # else:
                    #     results.append('out of stock')
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                        self.VARUS_SPECIAL_DIV_CLASS).text

                            results[2] = self.varus_price
                            # if self.varus_price:
                            #     results.append(self.varus_price)
                            # else:
                            #     results.append('out of stock')
                        except Exception as ex:
                            print(ex)
                            if ex:
                                try:
                                    self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                                self.VARUS_DISCOUNT_DIV_CLASS).text

                                    results[2] = self.varus_price
                                    # if self.varus_price:
                                    #     results.append(self.varus_price)
                                    # else:
                                    #     results.append('out of stock')
                                except Exception as ex:
                                    print(ex)


        return results
        # print(f'Полученные цены: \n---------------\nАТБ: {self.atb_price[:5]} \nEKO: {self.eko_price[:5]}\nVarus: {self.varus_price[:5]}')
        # print(f'Запросов сделано : {i}')
        # return self.atb_price, self.eko_price, self.varus_price

    def obolon_premium_parser(self):
        '''Парсер для сбора данных о цене продукта "Оболонь Премиум Экстра 1.1 л"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46',
                'https://eko.zakaz.ua/uk/products/pivo-obolon-1100ml-ukrayina--04820000190008/'
            ]
        )

    def vodka_getman_ICE_parcer(self):
        '''Парсер для сбора данных о цене продукта "Водка Гетьман ICE 0,7 л"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/gorilka-05l-getman-ice-40'
            ]
        )

    def coca_cola_2l_parcer(self):
        '''Парсер для сбора данных о цене продукта "напиток Coca-Cola 2 л"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/napij-225-l-coca-cola-bezalkogolnij-silnogazovanij',
                'https://eko.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
                'https://varus.ua/napiy-coca-cola-silnogazovaniy-2-l'
            ]
        )

    def garlik_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чеснок, кг" '''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/casnik-import-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-chasnik--ekomarket00000000640012/',
                'https://varus.ua/chasnik-vag'
            ]
        )

    def tea_minutka_black_40_b_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чай Минутка, 40 п, черный"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/caj-40-fp-h-14-g-minutka-black-tea-cornij-z-bergamotom-polsa',
                'https://eko.zakaz.ua/uk/products/chai-56g--05900396000972/'
            ]
        )

    def apple_golden_parcer(self):
        '''Парсер для сбора данных о цене продукта яблоко Голден'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/abluko-golden-1-gat',
                'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000641182/',
                'https://varus.ua/yabluko-golden-1-gatunok-vag'
            ]
        )

    def kent_8_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Кент 8'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/sigareti-kent-silver-25',
                'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683371/',
                'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08'
            ]
        )

    def coffee_aroma_gold_parcer(self):
        '''Парсер для сбора данных о цене продукта кофе растовримый Арома Голд'''
        return self.prices_parsing(
            [
                'https://eko.zakaz.ua/uk/products/kava--04771632312880/'
            ]
        )

    def oil_shedriy_dar_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Масло подсолнечное рафинированное Щедрый Дар 850 мл"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/olia-085l-sedrij-dar-sonasnikova-rafinovana',
                'https://eko.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
            ]
        )

    def fairy_limon_500_parcer(self):
        '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/zasib-miucij-dla-posudu-05l-fairy-sokovitij-limon',
                'https://eko.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
                'https://varus.ua/zasib-d-posudu-sokovit-limon-fairy-500ml'
            ]
        )

    def onion_parcer(self):
        '''Парсер для сбора данных о цене продукта лук'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/cibula-ripcasta-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
                'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
            ]
        )

    def apple_black_prince_parcer(self):
        '''Парсер для сбора данных о цене продукта "Яблоко Черный Принц"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/abluko-red-princ-1gat',
                'https://eko.zakaz.ua/uk/products/frukt-iabluka-bez-tm--ekomarket00000000645795/',
                'https://varus.ua/yabloko-princ-vag'
            ]
        )

    def smetana_stolica_smaky_400_20(self):
        '''Парсер для сбора данных о цене продукта "Сметана Столиця Смаку 400 гр 20% жирности"'''
        return self.prices_parsing(
            [
                'https://varus.zakaz.ua/uk/products/ukrayina--04820194043531/'
            ]
        )

    def limon_parcer(self):
        '''Парсер для сбора данных о цене продукта лимон'''
        return self.prices_parsing(
            [
                'https://atbmarket.com/product/limon-1-gat',
                'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000650210/',
                'https://varus.ua/limon-vag'
            ]
        )

result = ProductParserVol2()
print(result.coffee_aroma_gold_parcer())

# product_urls=[
#     'https://www.atbmarket.com/product/mandarini-1gat',
#     'https://eko.zakaz.ua/uk/products/frukt-iabluka-ukrayina--ekomarket00000000672673/',
#     'https://varus.ua/yabluko-golden-delishes-vag'
# ]
#
# res=ProductParserVol2()
# res.prices_parsing(product_urls)
