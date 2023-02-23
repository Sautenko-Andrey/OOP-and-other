# import requests
# from bs4 import BeautifulSoup
import undetected_chromedriver
from selenium.webdriver.common.by import By


class ProductParserVol2:
    '''Класс для парсинга цен с сайтов с приминением Selenium'''

    # количество досуипных маркетов
    COUNT_MARKETS = 3

    SELECTOR = By.CSS_SELECTOR
    ATB_REGULAR_DIV_CLASS = '[class="product-price__top"]'
    EKO_REGULAR_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title"]'
    EKO_DISCOUNT_DIV_CLASS = '[class="jsx-2be52a4b5bdfcc8a Price__value_title Price__value_discount"]'
    VARUS_REGULAR_DIV_CLASS = '[class="sf-price__regular"]'
    VARUS_SPECIAL_DIV_CLASS = '[class="sf-price__special"]'
    VARUS_DISCOUNT_DIV_CLASS = '[class="jsx-161433026 Price__value_title Price__value_discount"]'
    SILPO_REGULAR_DIV_CLASS='[class="current-integer"]'
    ASHAN_DIV_CLASS='[class="productDetails_price_actual__12u8E"]'

    def __init__(self):
        '''Инииализация драйвера Chrome со всеми нужными параметрами,
        а именно включение режима работы браузера в фоновом режиме'''
        self.options = undetected_chromedriver.ChromeOptions()
        # self.options.add_argument('enable-features=NetworkServiceInProcess')
        self.options.add_argument("disable-features=NetworkService")  # если верхнее не работает,то включаем это
        # self.options.add_argument("--disable-gpu")
        self.options.add_argument('--headless')
        self.driver = undetected_chromedriver.Chrome(options=self.options)

    def prices_parsing(self, urls: list):
        results = [0, 0, 0, 0, 0]
        '''Парсинг цен для продукта сразу со всех досутпных маркетов.'''
        for url in urls:
            if url[:15] == 'https://www.atb':
                # парсим цену АТБ
                self.driver.get(url)
                try:
                    self.atb_price = self.driver.find_element(self.SELECTOR, self.ATB_REGULAR_DIV_CLASS).text
                    results[0] = float(self.atb_price[:5])
                except Exception as ex:
                    print(ex)
            elif url[:11] == 'https://eko':
                # парсим цену ЭКО
                self.driver.get(url)
                try:
                    self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_REGULAR_DIV_CLASS).text
                    results[1] = float(self.eko_price[:5])
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.eko_price = self.driver.find_element(self.SELECTOR, self.EKO_DISCOUNT_DIV_CLASS).text
                            results[1] = float(self.eko_price[:5])
                        except Exception as ex:
                            print(ex)
            elif url[:13] == 'https://varus':
                # парсим цену Varus
                self.driver.get(url)
                try:
                    self.varus_price = self.driver.find_element(self.SELECTOR, self.VARUS_REGULAR_DIV_CLASS).text
                    results[2] = float(self.varus_price[:5])
                except Exception as ex:
                    print(ex)
                    if ex:
                        try:
                            self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                        self.VARUS_SPECIAL_DIV_CLASS).text
                            results[2] = float(self.varus_price[:5])
                        except Exception as ex:
                            print(ex)
                            if ex:
                                try:
                                    self.varus_price = self.driver.find_element(self.SELECTOR,
                                                                                self.VARUS_DISCOUNT_DIV_CLASS).text
                                    results[2] = float(self.varus_price[:5])
                                except Exception as ex:
                                    print(ex)
            elif url[:18] == 'https://shop.silpo':
                # парсим цену Сильпо
                self.driver.get(url)
                try:
                    self.silpo_price = self.driver.find_element(self.SELECTOR, self.SILPO_REGULAR_DIV_CLASS).text
                    self.driver.implicitly_wait(5)
                    results[3] = float(self.silpo_price[:5])
                except Exception as ex:
                    print(ex)
            elif url[:14] == 'https://auchan':
                # парсим цену Ашан
                self.driver.get(url)
                try:
                    self.ashan_price = self.driver.find_element(self.SELECTOR, self.ASHAN_DIV_CLASS).text
                    self.driver.implicitly_wait(5)
                    self.ashan_price=self.ashan_price.replace(',','.')
                    results[4] = float(self.ashan_price[:5])
                except Exception as ex:
                    print(ex)
        return results

    def obolon_premium_parser(self):
        '''Парсер для сбора данных о цене продукта "Оболонь Премиум Экстра 1.1 л"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46',
                'https://eko.zakaz.ua/uk/products/pivo-obolon-1100ml-ukrayina--04820000190008/'])

    def vodka_getman_ICE_parcer(self):
        '''Парсер для сбора данных о цене продукта "Водка Гетьман ICE 0,7 л"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/gorilka-05l-getman-ice-40'])

    def coca_cola_2l_parcer(self):
        '''Парсер для сбора данных о цене продукта "напиток Coca-Cola 2 л"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/napij-225-l-coca-cola-bezalkogolnij-silnogazovanij',
                'https://eko.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
                'https://varus.ua/napiy-coca-cola-silnogazovaniy-2-l',
                'https://shop.silpo.ua/product/napii-coca-cola-117',
                'https://auchan.ua/ua/napitok-bezalkogol-nyj-sil-nogazirovannyj-coca-cola-p-but-2l-688465/'])

    def garlik_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чеснок, кг" '''
        return self.prices_parsing(['https://www.atbmarket.com/product/casnik-import-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-chasnik--ekomarket00000000640012/',
                'https://varus.ua/chasnik-vag',
                'https://shop.silpo.ua/product/chasnyk-32595'])

    def tea_minutka_black_40_b_parcer(self):
        '''Парсер для сбора данных о цене продукта "Чай Минутка, 40 п, черный"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/caj-40-fp-h-14-g-minutka-black-tea-cornij-z-bergamotom-polsa',
                'https://eko.zakaz.ua/uk/products/chai-56g--05900396000972/'])

    def apple_golden_parcer(self):
        '''Парсер для сбора данных о цене продукта яблоко Голден'''
        return self.prices_parsing(['https://www.atbmarket.com/product/abluko-golden-1-gat',
                'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000641182/',
                'https://varus.ua/yabluko-golden-1-gatunok-vag',
                'https://shop.silpo.ua/product/yabluko-golden-zakarpattia-516860'])

    def kent_8_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Кент 8'''
        return self.prices_parsing(['https://www.atbmarket.com/product/sigareti-kent-silver-25',
                'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683371/',
                'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08',
                'https://shop.silpo.ua/product/tsygarky-kent-nd-navy-blue-907151'])

    def coffee_aroma_gold_parcer(self):
        '''Парсер для сбора данных о цене продукта кофе растовримый Арома Голд'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/kava--04771632312880/'])

    def oil_shedriy_dar_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Масло подсолнечное рафинированное Щедрый Дар 850 мл"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/olia-085l-sedrij-dar-sonasnikova-rafinovana',
                'https://eko.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
                'https://shop.silpo.ua/product/oliia-soniashnykova-shchedryi-dar-rafinovana-dezodorovana-890082',
                'https://auchan.ua/ua/maslo-podsolnechnoe-schedrij-dar-rafinirovannoe-850-ml-934363/'])

    def fairy_limon_500_parcer(self):
        '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/zasib-miucij-dla-posudu-05l-fairy-sokovitij-limon',
                'https://eko.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
                'https://varus.ua/zasib-d-posudu-sokovit-limon-fairy-500ml',
                'https://shop.silpo.ua/product/zasib-dlia-myttia-posudu-fairy-sokovytyi-lymon-48923'])

    def onion_parcer(self):
        '''Парсер для сбора данных о цене продукта лук'''
        return self.prices_parsing(['https://www.atbmarket.com/product/cibula-ripcasta-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
                'https://varus.ua/cibulya-ripchasta-1-gatunok-vag',
                'https://shop.silpo.ua/product/tsybulia-ripchasta-zhovta-32573'])

    def apple_black_prince_parcer(self):
        '''Парсер для сбора данных о цене продукта "Яблоко Черный Принц"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/abluko-red-princ-1gat',
                'https://eko.zakaz.ua/uk/products/frukt-iabluka-bez-tm--ekomarket00000000645795/',
                'https://varus.ua/yabloko-princ-vag',
                'https://shop.silpo.ua/product/yabluko-red-prynts-523750'])

    def smetana_stolica_smaky_400_20(self):
        '''Парсер для сбора данных о цене продукта "Сметана Столиця Смаку 400 гр 20% жирности"'''
        return self.prices_parsing(['https://varus.zakaz.ua/uk/products/ukrayina--04820194043531/'])

    def limon_parcer(self):
        '''Парсер для сбора данных о цене продукта лимон'''
        return self.prices_parsing(['https://atbmarket.com/product/limon-1-gat',
                'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000650210/',
                'https://varus.ua/limon-vag',
                'https://shop.silpo.ua/product/lymon-32550'])

    def oil_oleyna_neraf_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Масло подсолнечное Олейна нерафинированное 850 гр"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/oliia-oleina-900ml--04820077083500/'])

    def tea_monomah_black_kenya_90_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Чай черный листовой Мономах Кения 90 гр"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/chai-monomakh-90g--04820097812197/'])

    def arko_cool_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(['https://atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-cool',
                'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
                'https://varus.ua/pina-dlya-golinnya-kul-arko-200ml',
                'https://shop.silpo.ua/product/pina-dlia-golinnia-arko-prokholoda-166950'])

    def arko_sensitive_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-sensitive-promo',
                'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
                'https://varus.ua/pina-dlya-golinnya-ekstra-sensitiv-arko-200ml',
                'https://shop.silpo.ua/product/pina-dlia-golinnia-arko-dlia-chutlyvoi-shkiry-44192'])

    def carrot_parcer(self):
        '''Парсер для сбора данных о цене продукта морковь'''
        return self.prices_parsing(['https://www.atbmarket.com/product/morkva-1gat',
                'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
                'https://varus.ua/morkva-1-gatunok-vag',
                'https://shop.silpo.ua/product/morkva-myta-367056'])

    def cabbage_parcer(self):
        '''Парсер для сбора данных о цене продукта капуста'''
        return self.prices_parsing(['https://www.atbmarket.com/product/kapusta-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
                'https://varus.ua/kapusta-1-gatunok-vag',
                'https://shop.silpo.ua/product/kapusta-bilogolova-32572'])

    def egg_parcer(self):
        '''Парсер для сбора данных о цене продукта яйца куринные'''
        return self.prices_parsing(['https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas',
                'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/',
                'https://varus.ua/yayce-kuryache-1sht',
                'https://shop.silpo.ua/product/yaitsia-kuriachi-povna-chasha-1-kategoriia-435227'])

    def mayonez_detsk_shedro_67_parcer(self):
        '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%"'''
        return self.prices_parsing(['https://www.atbmarket.com/product/majonez-190g-sedro-domasnij-dla-ditej-67',
                'https://eko.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
                'https://varus.ua/mayonez-domashniy-dlya-ditey-67-schedro-190g-d-p-ukraina',
                'https://shop.silpo.ua/product/maionez-shchedro-domashnii-dlia-ditei-67-685628'])

    def rexona_aloe_vera_w_parcer(self):
        '''Парсер для сбора данных о цене продукта "Дезодорант Rexona Aloe Vera женский"'''
        return self.prices_parsing(['https://eko.zakaz.ua/uk/products/dezodorant-reksona-150ml-velikobritaniia--08712561844338/'])

    def marloboro_red_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Мальборо красные'''
        return self.prices_parsing(['https://www.atbmarket.com/product/sigareti-marlboro-27',
                'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003205557/',
                'https://varus.ua/cigarki-marlboro',
                'https://shop.silpo.ua/product/sygarety-marlboro-red-911500',
                'https://auchan.ua/ua/sigarety-marlboro-20-sht-916786/'])

    def beer_lvivske_svitle_24l(self):
        '''Парсер для сбора данных о цене продукта "Пиво ЛЬвовское светлое 2,4 литра"'''
        return self.prices_parsing(
            ['https://varus.ua/pivo-2-4l-4-5-svitle-pasteriz-lvivske',
             'https://shop.silpo.ua/product/pyvo-lvivske-svitle-812957'])

    def smetana_stolica_smaky_400_15_parcer(self):
        '''Парсер для сбора данных о цене продукта сметана "Столица Смаку 400 гр 15%"'''
        return self.prices_parsing(['https://varus.zakaz.ua/ru/products/ukrayina--04820194043517/'])

    def water_in_6l_bottle_parser(self):
        '''Парсер для сбора данных о цене продукта вода питьевая в 6 литровой бутылке'''
        return self.prices_parsing(['https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana',
                'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/',
                'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'])

    def pork_lopatka_parser(self):
        '''Парсер для сбора данных о цене продукта свинина лопатка/на кости, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/okist-lembergmit-svinacij-oholodzenij-vakupak',
                'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000535086/',
                'https://varus.ua/lopatka-svinaya-vesovaya'])

    def potato_parser(self):
        '''Парсер для сбора данных о цене продукта картошка обыкновенная, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/kartopla-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
                'https://varus.ua/kartoplya-1-gatunok-vag'])

    def beet_parser(self):
        '''Парсер для сбора данных о цене продукта буряк обыкновенный, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/burak-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/',
                'https://varus.ua/buryak-1-gatunok-vag',
                'https://shop.silpo.ua/product/buriak-32570'])

    def four_parser(self):
        '''Парсер для сбора данных о цене продукта муки, кг'''
        return self.prices_parsing(['https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok',
                'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/',
                'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'])

    def oil_for_dishes_parser(self):
        '''Парсер масла для приготовки блюд(самое популярное) '''
        return self.prices_parsing(['https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana',
                'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/',
                'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'])

    def sour_cream_for_dishes_parser(self):
        '''Парсер для самой популярной сметаны к блюдам (вареники, борщ, т.д.)'''
        return self.prices_parsing(['https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan',
                'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/',
                'https://varus.ua/smetana-yagotinska-15-450g'])

    def desodorant_garnier_magniy_man_parser(self):
        '''Парсер для дезодоранта "Garnier Магний мужской"'''
        return self.prices_parsing(['https://shop.silpo.ua/product/dezodorant-sprei-garnier-men-magnii-ultrasukhist-813133'])

class AllDishParsersVol2(ProductParserVol2):
    '''Класс в котором собраны парсеры для блюд'''
    # количество доступных маркетов

    # добавочные ингридиенты
    TOMAT_PASTE_VALUE, OIL_VALUE, LIMON_ACID_VALUE, SOLT_VALUE, LAVR_LIST_VALUE = 1, 1, 1, 1, 1
    def dish_red_borsh_parser(self):
        '''Парсинг цены красного борща в доступных супермаркетах'''
        # соберем все цены ингридиентов для приготовления борща
        water = self.water_in_6l_bottle_parser()
        pork = self.pork_lopatka_parser()
        potato = self.potato_parser()
        beet = self.beet_parser()
        carrot = self.carrot_parcer()
        onion = self.onion_parcer()
        cabbage = self.cabbage_parcer()

        results = []
        for i in range(self.COUNT_MARKETS):
            result = round((float(water[i]) / 3 + float(pork[i]) * 0.8 +
                            float(potato[i]) / 2 + float(beet[i]) / 10 +
                            float(carrot[i]) / 10 + float(onion[i]) * 0.2 +
                            float(cabbage[i]) * 0.4 + self.TOMAT_PASTE_VALUE +
                            self.OIL_VALUE + self.LIMON_ACID_VALUE +
                            self.SOLT_VALUE + self.LAVR_LIST_VALUE) / 6, 2)
            results.append(result)
        return results

    def dish_vareniki_s_kartoshkoy_parser(self):
        '''Парсинг цены вареников с картошкой в доступных супермаркетах'''
        # соберем все цены ингридиентов для приготовления вареников с картошкой
        flour = self.four_parser()
        water = self.water_in_6l_bottle_parser()
        eggs = self.egg_parcer()
        eggs[0] = eggs[0] / 10  # атб яйца разделить на 10
        oil = self.oil_for_dishes_parser()
        onion = self.onion_parcer()
        smetana = self.sour_cream_for_dishes_parser()
        potato = self.potato_parser()

        results = []
        for i in range(self.COUNT_MARKETS):
            result = round((float(flour[i]) * 0.4 + float(water[i]) * 0.033 +
                            float(eggs[i]) + float(oil[i]) * 0.05 +
                            float(onion[i]) * 0.2 + float(smetana[i]) +
                            float(potato[i]) * 0.6 + self.SOLT_VALUE) / 5, 2)
            results.append(result)
        return results

    def dish_vareniki_s_kapustoy_parser(self):
        '''Парсер для вареников с капустой'''
        # соберем все цены ингридиентов для приготовления вареников с капустой
        flour = self.four_parser()
        water = self.water_in_6l_bottle_parser()
        eggs = self.egg_parcer()
        eggs[0] = eggs[0] / 10  # атб яйца разделить на 10
        oil = self.oil_for_dishes_parser()
        onion = self.onion_parcer()
        smetana = self.sour_cream_for_dishes_parser()
        cabbage = self.cabbage_parcer()

        results = []
        for i in range(self.COUNT_MARKETS):
            result = round((float(flour[i]) * 0.4 + float(water[i]) * 0.033 +
                            float(eggs[i]) + float(oil[i]) * 0.05 +
                            float(onion[i]) * 0.2 + float(smetana[i]) +
                            float(cabbage[i]) * 0.6 + self.SOLT_VALUE) / 5, 2)
            results.append(result)
        return results





# class ProductParsers:
#     '''Класс для хранения парсеров для всех продуктов приложения'''
#     ATB_CLASS = 'product-price__top'
#     EKO_CLASS = 'jsx-161433026 Price__value_title'
#     EKO_DISCOUNT_CLASS = 'jsx-161433026 Price__value_title Price__value_discount'
#     VARUS_CLASS = 'sf-price__regular'
#     VARUS_SPECIAL_CLASS = 'sf-price__special'
#     VARUS_DISCOUNT_CLASS = 'jsx-161433026 Price__value_title Price__value_discount'
#
#     HEADERS = {
#         'Accept': '*/*',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
#     }
#
#     def price_parcing_find_next(self, page_url: str, class_: str):
#         url = page_url
#         headers = self.HEADERS
#         req = requests.get(url, headers=headers)
#         src = req.text
#         soup = BeautifulSoup(src, 'html.parser')
#         price = soup.find(class_=class_).find_next().text
#         return price
#
#     def price_parcing(self, page_url: str, class_: str):
#         url = page_url
#         headers = self.HEADERS
#         req = requests.get(url, headers=headers)
#         src = req.text
#         soup = BeautifulSoup(src, 'html.parser')
#         price = soup.find(class_=class_).text
#         return price
#
#     def obolon_premium_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Оболонь Премиум Экстра 1.1 л"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46',
#             self.ATB_CLASS)
#
#         # # прописываем адресс страницы с пивом Оболонь Премиум Экстра 1.1 л
#         # url = 'https://www.atbmarket.com/product/pivo-11l-obolon-premium-extra-brew-svitle-alk-46'
#         #
#         # # создадим заголовки
#         # headers = {
#         #     'Accept': '*/*',
#         #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
#         # }
#         #
#         # # переменная req будет нам возвращать результат работы метода get библиотеки requests.
#         # # В аргументах указываем url сайта и наши заголовки:
#         # req = requests.get(url, headers=headers)
#         #
#         # # сохраним в переменную src полученный объект и вызовем у него метод text:
#         # src = req.text
#         #
#         # # далее сохраним нашу страницу в файл.
#         # # Т.к. многие сайты не любят, когда их парсят и велика вероятность получения бана
#         # # или ограничения по времени за большое количество запросов.
#         # # А сохранив страницу мы всегда можем продолжить работать с ней дальше.
#         # # with open('products_data/obolon_premium_(1.1).html','w') as f:
#         # #     f.write(src)
#         # #
#         # # #Далее откроем, прочитаем и сохраним наш файл страницы в переменную:
#         # # with open('products_data/obolon_premium_(1.1).html') as f:
#         # #     src=f.read()
#         #
#         # # создадим объект BeautifulSoup и передадим ему нашу переменную src
#         # # и парсер html.parser приступим к сбору данных:
#         # soup = BeautifulSoup(src, 'html.parser')
#         #
#         # # получаем цену пива:
#         # obolon_price = soup.find(class_='product-price__top').find_next().text
#         #
#         # return obolon_price
#
#     def beer_obolon_premium_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing('https://eko.zakaz.ua/uk/products/pivo-obolon-1100ml-ukrayina--04820000190008/',
#                                   self.EKO_CLASS)
#
#     def vodka_getman_ICE_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Водка Гетьман ICE 0,7 л"'''
#         return self.price_parcing_find_next('https://www.atbmarket.com/product/gorilka-05l-getman-ice-40',
#                                             self.ATB_CLASS)
#
#     def coca_cola_2l_parcer(self):
#         '''Парсер для сбора данных о цене продукта "напиток Coca-Cola 2 л"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/napij-225-l-coca-cola-bezalkogolnij-silnogazovanij',
#             self.ATB_CLASS)
#
#     def coca_cola_2l_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/napii-koka-kola-2000ml--05449000009067/',
#             self.EKO_CLASS
#         )
#
#     def coca_cola_2l_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Пиво Оболонь Премиум 1.1 л в Эко-Маркете"'''
#         return self.price_parcing(
#             'https://varus.ua/napiy-coca-cola-silnogazovaniy-2-l',
#             self.VARUS_CLASS
#         )[:5]
#
#     def garlik_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чеснок, кг" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/casnik-import-1-gat',
#             self.ATB_CLASS
#         )
#
#     def garlik_eko_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чеснок, кг" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-chasnik--ekomarket00000000640012/',
#             self.EKO_CLASS
#         )
#
#     def garlik_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта чеснок из Varus'''
#         return self.price_parcing(
#             'https://varus.ua/chasnik-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def tea_minutka_black_40_b_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чай Минутка, 40 п, черный"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/caj-40-fp-h-14-g-minutka-black-tea-cornij-z-bergamotom-polsa',
#             self.ATB_CLASS
#         )
#
#     def tea_minutka_black_40_b_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Чай Минутка 40 пак чорный" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/chai-56g--05900396000972/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def apple_golden_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/abluko-golden-1-gat',
#             self.ATB_CLASS
#         )
#
#     def apple_golden_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из ЭКО-МАРКЕТА'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-iabluka--ekomarket00000000641182/',
#             self.EKO_CLASS
#         )
#
#     def apple_golden_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта яблоко Голден из Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yabluko-golden-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def kent_8_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта сигареты Кент 8 из ЭКО-МАРКЕТА'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/tsigarki-kent--04820192683371/',
#             self.EKO_CLASS
#         )
#
#     def kent_8_atb_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Kent 8" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/sigareti-kent-silver-25',
#             self.ATB_CLASS
#         )
#
#     def kent_8_varus_parcer(self):
#         '''Парсер для сбора данных о цене продукта сигареты Kent 8'''
#         return self.price_parcing(
#             'https://varus.ua/cigarki-kent-navy-blue-4-0-8-08',
#             self.VARUS_CLASS
#         )[:5]
#
#     def coffee_aroma_gold_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта кофе растовримый Арома Голд'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/kava--04771632312880/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def oil_shedriy_dar_850_atb_parcer(self):
#         '''Парсер для сбора данных о цене продукта "Масло подсолнечное рафинированное Щедрый Дар 850 мл"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/olia-085l-sedrij-dar-sonasnikova-rafinovana',
#             self.ATB_CLASS
#         )
#
#     def oil_shedriy_dar_850_ekomarket_parcer(self):
#         '''Парсер для сбора данных о цене продукта
#          масло подсолнечное рафинированное Щедрый Дар 850 мл из Эко-Маркета'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/oliia-shchedrii-dar-850ml--04820078575769/',
#             self.EKO_CLASS
#         )
#
#     def fairy_limon_500_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/zasib-miucij-dla-posudu-05l-fairy-sokovitij-limon',
#             self.ATB_CLASS
#         )
#
#     def fairy_limon_500_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/zasib-feiri-500ml-ukrayina--05413149313842/',
#             self.EKO_CLASS
#         )
#
#     def fairy_limon_500_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Fairy лимон, 500 млг"'''
#         return self.price_parcing(
#             'https://varus.ua/zasib-d-posudu-sokovit-limon-fairy-500ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def onion_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта лук в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/cibula-ripcasta-1-gat',
#             self.ATB_CLASS
#         )
#
#     def onion_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта лук в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/',
#             self.EKO_CLASS
#         )
#
#     def onion_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта лук в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/cibulya-ripchasta-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def apple_black_prince_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный Принц" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/abluko-red-princ-1gat',
#             self.ATB_CLASS
#         )
#
#     def apple_black_prince_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный принц" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-iabluka-bez-tm--ekomarket00000000645795/',
#             self.EKO_CLASS
#         )
#
#     def apple_black_prince_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Яблоко Черный принц" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yabloko-princ-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def smetana_stolica_smaky_400_20_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Сметана Столиця Смаку 400 гр 20% жирности" в Varus'''
#         return self.price_parcing(
#             'https://varus.zakaz.ua/uk/products/ukrayina--04820194043531/',
#             self.VARUS_DISCOUNT_CLASS
#         )[:5]
#
#     def limon_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта лимон в АТБ'''
#         return self.price_parcing_find_next(
#             'https://atbmarket.com/product/limon-1-gat',
#             self.ATB_CLASS
#         )
#
#     def limon_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта лимон в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/frukt-tsitrus--ekomarket00000000650210/',
#             self.EKO_CLASS
#         )
#
#     def limon_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта лимон в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/limon-vag',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def oil_oleyna_neraf_850_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Масло подсолнечное Олейна нерафинированное 850 гр" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/oliia-oleina-900ml--04820077083500/',
#             self.EKO_CLASS
#         )
#
#     def tea_monomah_black_kenya_90_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Чай черный листовой Мономах Кения 90 гр" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/chai-monomakh-90g--04820097812197/',
#             self.EKO_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-cool',
#             self.ATB_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
#             self.EKO_CLASS
#         )
#
#     def arko_cool_200_bonus100_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pina-dlya-golinnya-kul-arko-200ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def arko_sensitive_200_bonus100_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-sensitive-promo',
#             self.ATB_CLASS
#         )
#
#     def arko_sensitive_200_bonus100_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
#             self.EKO_CLASS
#         )
#
#     def arko_sensitive_200_bonus100_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pina-dlya-golinnya-ekstra-sensitiv-arko-200ml',
#             self.VARUS_SPECIAL_CLASS
#         )[:5]
#
#     def carrot_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/morkva-1gat',
#             self.ATB_CLASS
#         )
#
#     def carrot_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 200 млг+100млг бонус" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
#             self.EKO_CLASS
#         )
#
#     def carrot_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Пена для бритья ARKO Cool 300 млг+100млг бонус" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/morkva-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def cabbage_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта капуста в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/kapusta-1-gat',
#             self.ATB_CLASS
#         )
#
#     def cabbage_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта капуста в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
#             self.EKO_CLASS
#         )
#
#     def cabbage_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта капуста в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/kapusta-1-gatunok-vag',
#             self.VARUS_CLASS
#         )[:5]
#
#     def egg_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в АТБ'''
#         return float(self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas',
#             self.ATB_CLASS
#         )) / 10
#
#     def egg_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/',
#             self.EKO_CLASS
#         )
#
#     def egg_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта яйца куринные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/yayce-kuryache-1sht',
#             self.VARUS_CLASS
#         )[:5]
#
#     def mayonez_detsk_shedro_67_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/majonez-190g-sedro-domasnij-dla-ditej-67',
#             self.ATB_CLASS
#         )
#
#     def mayonez_detsk_shedro_67_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
#             self.EKO_CLASS
#         )
#
#     def mayonez_detsk_shedro_67_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%" в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/mayonez-domashniy-dlya-ditey-67-schedro-190g-d-p-ukraina',
#             self.VARUS_CLASS
#         )[:5]
#
#     def rexona_aloe_vera_w_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта "Дезодорант Rexona Aloe Vera женский" в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/dezodorant-reksona-150ml-velikobritaniia--08712561844338/',
#             self.EKO_DISCOUNT_CLASS
#         )
#
#     def marloboro_red_parcer_ATB(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в АТБ'''
#         return self.price_parcing_find_next(
#             'https://www.atbmarket.com/product/sigareti-marlboro-27',
#             self.ATB_CLASS
#         )
#
#     def marloboro_red_parcer_EKO(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Эко-Маркете'''
#         return self.price_parcing(
#             'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003205557/',
#             self.EKO_CLASS
#         )
#
#     def marloboro_red_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/cigarki-marlboro',
#             self.VARUS_CLASS
#         )[:5]
#
#     def beer_lvivske_svitle_24l_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сигареты Мальборо красные в Varus'''
#         return self.price_parcing(
#             'https://varus.ua/pivo-2-4l-4-5-svitle-pasteriz-lvivske',
#             self.VARUS_CLASS
#         )[:5]
#
#     def smetana_stolica_smaky_400_15_parcer_VARUS(self):
#         '''Парсер для сбора данных о цене продукта сметана "Столица Смаку 400 гр 15%" в Varus'''
#         return self.price_parcing(
#             'https://varus.zakaz.ua/ru/products/ukrayina--04820194043517/',
#             self.VARUS_DISCOUNT_CLASS
#         )[:5]
#
#     def dollar_value_parcer(self):
#         '''Парсер для отображения текущего курса доллара в обменниках'''
#         return self.price_parcing(
#             'https://finance.ua/ru/',
#             'fua-xrates__value'
#         )
#
#
# class AllDishParsers:
#     '''Класс в котором собраны парсеры для борща'''
#
#     # создадим заголовки
#     headers = {
#         'Accept': 'image/avif,image/webp,*/*',
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
#     }
#
#     def dish_red_borsh_parser_atb(self):
#         '''Парсер для борща'''
#         # прописываем адресс страницы:
#         # для воды:
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         # для свинины:
#         pork_url = 'https://www.atbmarket.com/product/okist-lembergmit-svinacij-oholodzenij-vakupak'
#         # для картошки
#         potato_url = 'https://www.atbmarket.com/product/kartopla-1-gat'
#         # для буряка
#         beet_url = 'https://www.atbmarket.com/product/burak-1-gat'
#         # для морковки
#         carrot_url = 'https://www.atbmarket.com/product/morkva-1gat'
#         # для лука
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         # для капусты
#         cabbage_url = 'https://www.atbmarket.com/product/kapusta-1-gat'
#
#         # переменная req будет нам возвращать результат работы метода get библиотеки requests.
#         # В аргументах указываем url сайта и наши заголовки:
#         water_req = requests.get(water_url, headers=self.headers)
#         pork_req = requests.get(pork_url, headers=self.headers)
#         potato_req = requests.get(potato_url, headers=self.headers)
#         beet_req = requests.get(beet_url, headers=self.headers)
#         carrot_req = requests.get(carrot_url, headers=self.headers)
#         onion_req = requests.get(onion_url, headers=self.headers)
#         cabbage_req = requests.get(cabbage_url, headers=self.headers)
#
#         # сохраним в переменную src полученный объект и вызовем у него метод text:
#         water_src = water_req.text
#         pork_src = pork_req.text
#         potato_src = potato_req.text
#         beet_src = beet_req.text
#         carrot_src = carrot_req.text
#         onion_src = onion_req.text
#         cabbage_src = cabbage_req.text
#
#         # создадим объект BeautifulSoup и передадим ему нашу переменную src
#         # и парсер html.parser приступим к сбору данных:
#         water_soup = BeautifulSoup(water_src, 'html.parser')
#         pork_soup = BeautifulSoup(pork_src, 'html.parser')
#         potato_soup = BeautifulSoup(potato_src, 'html.parser')
#         beet_soup = BeautifulSoup(beet_src, 'html.parser')
#         carrot_soup = BeautifulSoup(carrot_src, 'html.parser')
#         onion_soup = BeautifulSoup(onion_src, 'html.parser')
#         cabbage_soup = BeautifulSoup(cabbage_src, 'html.parser')
#
#         # получаем цены всех ингридиентов:
#         water_value = float(water_soup.find(class_='product-price__top').find_next().text) / 3
#         pork_value = float(pork_soup.find(class_='product-price__top').find_next().text) * 0.8
#         potato_value = float(potato_soup.find(class_='product-price__top').find_next().text) / 2
#         beet_value = float(beet_soup.find(class_='product-price__top').find_next().text) / 10
#         carrot_value = float(carrot_soup.find(class_='product-price__top').find_next().text) / 10
#         onion_value = float(onion_soup.find(class_='product-price__top').find_next().text) * 0.2
#         cabbage_value = float(cabbage_soup.find(class_='product-price__top').find_next().text) * 0.4
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = (water_value + pork_value +
#                      potato_value + beet_value +
#                      carrot_value + onion_value +
#                      cabbage_value + tomat_paste_value +
#                      oil_value + limon_acid_value +
#                      solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_red_borsh_parser_eko(self):
#         '''Парсер для борща Эко-маркет'''
#
#         find_class = 'jsx-161433026 Price__value_title Price__value_discount'
#
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         pork_url = 'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000535086/'
#         potato_url = 'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/'
#         beet_url = 'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/'
#         carrot_url = 'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         cabbage_url = 'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/'
#
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         pork_soup = BeautifulSoup(requests.get(pork_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#         beet_soup = BeautifulSoup(requests.get(beet_url, headers=self.headers).text, 'html.parser')
#         carrot_soup = BeautifulSoup(requests.get(carrot_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         water_value = float(water_soup.find(class_=find_class).text) / 3
#         pork_value = float(pork_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.8
#         potato_value = float(potato_soup.find(class_='jsx-161433026 Price__value_title').text) / 2
#         beet_value = float(beet_soup.find(class_='jsx-161433026 Price__value_title').text) / 10
#         carrot_value = float(carrot_soup.find(class_='jsx-161433026 Price__value_title').text) / 10
#         onion_value = float(onion_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.2
#         cabbage_value = float(cabbage_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.4
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = (water_value + pork_value +
#                      potato_value + beet_value +
#                      carrot_value + onion_value +
#                      cabbage_value + tomat_paste_value +
#                      oil_value + limon_acid_value +
#                      solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_red_borsh_parser_varus(self):
#         '''Парсер для борща Varus'''
#
#         find_class = 'sf-price__regular'
#
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         pork_url = 'https://varus.ua/lopatka-svinaya-vesovaya'
#         potato_url = 'https://varus.ua/kartoplya-1-gatunok-vag'
#         beet_url = 'https://varus.ua/buryak-1-gatunok-vag'
#         carrot_url = 'https://varus.ua/morkva-1-gatunok-vag'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         cabbage_url = 'https://varus.ua/kapusta-1-gatunok-vag'
#
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         pork_soup = BeautifulSoup(requests.get(pork_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#         beet_soup = BeautifulSoup(requests.get(beet_url, headers=self.headers).text, 'html.parser')
#         carrot_soup = BeautifulSoup(requests.get(carrot_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         water_value = (water_soup.find(class_=find_class).text)
#         pork_value = (pork_soup.find(class_='sf-price__special').text)
#         potato_value = (potato_soup.find(class_='sf-price__special').text)
#         beet_value = (beet_soup.find(class_='sf-price__special').text)
#         carrot_value = (carrot_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         cabbage_value = (cabbage_soup.find(class_=find_class).text)
#         tomat_paste_value = 1
#         oil_value = 1
#         limon_acid_value = 1
#         solt_value = 1
#         lavr_list_value = 1
#
#         total_sum = ((float(water_value[:5]) / 3) + (float(pork_value[:5]) * 0.8) +
#                      (float(potato_value[:5]) / 2) + (float(beet_value[:5]) / 10) +
#                      (float(carrot_value[:5]) / 10) + (float(onion_value[:5]) * 0.2) +
#                      (float(cabbage_value[:5]) * 0.4) + tomat_paste_value + oil_value +
#                      limon_acid_value + solt_value + lavr_list_value) / 6
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_atb(self):
#         '''Парсер для вареников с картошкой АТБ'''
#
#         find_class = 'product-price__top'  # класс div по которому будем искать цену
#
#         flour_url = 'https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok'
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         egg_url = 'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas'
#         oil_url = 'https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana'
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         sour_cream_url = 'https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan'
#         potato_url = 'https://www.atbmarket.com/product/kartopla-1-gat'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).find_next().text) * 0.4
#         water_value = float(water_soup.find(class_=find_class).find_next().text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).find_next().text) * 0.1
#         oil_value = float(oil_soup.find(class_=find_class).find_next().text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).find_next().text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).find_next().text)
#         potato_value = float(potato_soup.find(class_=find_class).find_next().text) * 0.6
#         solt_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + potato_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_eko(self):
#         '''Парсер для вареников с картошкой ЭКО-МАркет'''
#
#         find_class = 'jsx-161433026 Price__value_title'
#
#         flour_url = 'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/'
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         egg_url = 'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/'
#         oil_url = 'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         sour_cream_url = 'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/'
#         potato_url = 'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).text) * 0.4
#         water_value = float(water_soup.find(class_=find_class).text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).text)
#         oil_value = float(oil_soup.find(class_=find_class).text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).text)
#         potato_value = float(potato_soup.find(class_='jsx-161433026 Price__value_title').text) * 0.6
#         solt_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      potato_value + solt_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kartoshkoy_varus(self):
#         '''Парсер для вареников с картошкой Varus'''
#
#         find_class = 'sf-price__regular'
#
#         flour_url = 'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         egg_url = 'https://varus.ua/yayce-kuryache-1sht'
#         oil_url = 'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         sour_cream_url = 'https://varus.ua/smetana-yagotinska-15-450g'
#         potato_url = 'https://varus.ua/kartoplya-1-gatunok-vag'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         potato_soup = BeautifulSoup(requests.get(potato_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = (flour_soup.find(class_=find_class).text)
#         water_value = (water_soup.find(class_=find_class).text)
#         egg_value = (egg_soup.find(class_=find_class).text)
#         oil_value = (oil_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         sour_cream_value = (sour_cream_soup.find(class_=find_class).text)
#         potato_value = (potato_soup.find(class_='sf-price__special').text)
#         solt_value = 1
#
#         total_sum = ((float(flour_value[:5]) * 0.4) + (float(water_value[:5]) * 0.033) +
#                      (float(egg_value[:5])) + (float(oil_value[:5]) * 0.05) +
#                      (float(onion_value[:5]) * 0.02) + (float(sour_cream_value[:5])) +
#                      (float(potato_value[:5]) * 0.6) + solt_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_atb(self):
#         '''Парсер для вареников с капустой'''
#
#         flour_url = 'https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok'
#         water_url = 'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana'
#         egg_url = 'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas'
#         oil_url = 'https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana'
#         onion_url = 'https://www.atbmarket.com/product/cibula-ripcasta-1-gat'
#         sour_cream_url = 'https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan'
#         cabbage_url = 'https://www.atbmarket.com/product/kapusta-1-gat'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_='product-price__top').find_next().text) * 0.4
#         water_value = float(water_soup.find(class_='product-price__top').find_next().text) * 0.033
#         egg_value = float(egg_soup.find(class_='product-price__top').find_next().text) * 0.1
#         oil_value = float(oil_soup.find(class_='product-price__top').find_next().text) * 0.05
#         onion_value = float(onion_soup.find(class_='product-price__top').find_next().text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_='product-price__top').find_next().text)
#         cabbage_value = float(cabbage_soup.find(class_='product-price__top').find_next().text) * 0.6
#         solt_value = 1
#         carrot_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + cabbage_value + carrot_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_eko(self):
#         '''Парсер для вареников с капустой Эко-маркет'''
#
#         find_class = 'jsx-161433026 Price__value_title'
#
#         flour_url = 'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/'
#         water_url = 'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/'
#         egg_url = 'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/'
#         oil_url = 'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/'
#         onion_url = 'https://eko.zakaz.ua/uk/products/ovochi-tsibulia--ekomarket00000000647281/'
#         sour_cream_url = 'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/'
#         cabbage_url = 'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = float(flour_soup.find(class_=find_class).text) * 0.4
#         water_value = float(
#             water_soup.find(class_='jsx-161433026 Price__value_title Price__value_discount').text) * 0.033
#         egg_value = float(egg_soup.find(class_=find_class).text) * 0.1
#         oil_value = float(oil_soup.find(class_=find_class).text) * 0.05
#         onion_value = float(onion_soup.find(class_=find_class).text) * 0.2
#         sour_cream_value = float(sour_cream_soup.find(class_=find_class).text)
#         cabbage_value = float(cabbage_soup.find(class_=find_class).text) * 0.6
#         solt_value = 1
#         carrot_value = 1
#
#         total_sum = (flour_value + water_value +
#                      egg_value + oil_value +
#                      onion_value + sour_cream_value +
#                      solt_value + cabbage_value + carrot_value) / 5
#
#         return total_sum
#
#     def dish_variniki_s_kapustoy_varus(self):
#         '''Парсер для вареников с капустой Эко-маркет'''
#
#         find_class = 'sf-price__regular'
#
#         flour_url = 'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'
#         water_url = 'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
#         egg_url = 'https://varus.ua/yayce-kuryache-1sht'
#         oil_url = 'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'
#         onion_url = 'https://varus.ua/cibulya-ripchasta-1-gatunok-vag'
#         sour_cream_url = 'https://varus.ua/smetana-yagotinska-15-450g'
#         cabbage_url = 'https://varus.ua/kapusta-1-gatunok-vag'
#
#         flour_soup = BeautifulSoup(requests.get(flour_url, headers=self.headers).text, 'html.parser')
#         water_soup = BeautifulSoup(requests.get(water_url, headers=self.headers).text, 'html.parser')
#         egg_soup = BeautifulSoup(requests.get(egg_url, headers=self.headers).text, 'html.parser')
#         oil_soup = BeautifulSoup(requests.get(oil_url, headers=self.headers).text, 'html.parser')
#         onion_soup = BeautifulSoup(requests.get(onion_url, headers=self.headers).text, 'html.parser')
#         sour_cream_soup = BeautifulSoup(requests.get(sour_cream_url, headers=self.headers).text, 'html.parser')
#         cabbage_soup = BeautifulSoup(requests.get(cabbage_url, headers=self.headers).text, 'html.parser')
#
#         flour_value = (flour_soup.find(class_=find_class).text)
#         water_value = (water_soup.find(class_=find_class).text)
#         egg_value = (egg_soup.find(class_=find_class).text)
#         oil_value = (oil_soup.find(class_=find_class).text)
#         onion_value = (onion_soup.find(class_=find_class).text)
#         sour_cream_value = (sour_cream_soup.find(class_=find_class).text)
#         cabbage_value = (cabbage_soup.find(class_=find_class).text)
#         solt_value = 1
#
#         total_sum = ((float(flour_value[:5]) * 0.4) + (float(water_value[:5]) * 0.033) +
#                      (float(egg_value[:5])) + (float(oil_value[:5]) * 0.05) +
#                      (float(onion_value[:5]) * 0.02) + (float(sour_cream_value[:5])) +
#                      (float(cabbage_value[:5]) * 0.6) + solt_value) / 5
#
#         return total_sum

    # def best_price_parcer(self):
    #     '''Парсер для сбора данных о акционной цене на некий товар'''
    #
    #     # прописываем адресс страницы с пивом Оболонь Премиум Экстра 1.1 л
    #     url_1 = 'https://www.atbmarket.com/product/sokolad-90g-millennium-poristij-bilij'
    #     url_2='https://www.atbmarket.com/product/vinograd-susenij-150g-svoa-linia-kismis-zolotistij'
    #     url_3='https://www.atbmarket.com/product/vino-075l-igriste-asti-salute-bile-solodke-9-12'
    #
    #
    #
    #     # создадим заголовки
    #     headers={
    #          'Accept':'*/*',
    #          'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
    #     }
    #
    #     # переменная req будет нам возвращать результат работы метода get библиотеки requests.
    #     # В аргументах указываем url сайта и наши заголовки:
    #     req_1=requests.get(url_1,headers=headers)
    #     req_2=requests.get(url_2,headers=headers)
    #     req_3 = requests.get(url_3, headers=headers)
    #
    #     #сохраним в переменную src полученный объект и вызовем у него метод text:
    #     src_1=req_1.text
    #     soup_1=BeautifulSoup(src_1,'html.parser')
    #
    #     src_2 = req_2.text
    #     soup_2 = BeautifulSoup(src_2, 'html.parser')
    #
    #     src_3 = req_3.text
    #     soup_3 = BeautifulSoup(src_3, 'html.parser')
    #
    #     #получаем цену товара:
    #     product_1_price=soup_1.find(class_='product-price__top').find_next().text
    #     product_2_price = soup_2.find(class_='product-price__top').find_next().text
    #     product_3_price = soup_3.find(class_='product-price__top').find_next().text
    #
    #     #получем название товара:
    #     product_1_name=soup_1.find(class_='page-title product-page__title').text
    #     product_2_name = soup_2.find(class_='page-title product-page__title').text
    #     product_3_name = soup_3.find(class_='page-title product-page__title').text
    #
    #     return product_1_price, product_1_name,\
    #         product_2_price, product_2_name,\
    #         product_3_price, product_3_name
