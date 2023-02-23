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
        results = [0, 0, 0]
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
        return results

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

    def oil_oleyna_neraf_850_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Масло подсолнечное Олейна нерафинированное 850 гр"'''
        return self.prices_parsing(
            [
                'https://eko.zakaz.ua/uk/products/oliia-oleina-900ml--04820077083500/'
            ]
        )

    def tea_monomah_black_kenya_90_parcer(self):
        '''Парсер для сбора данных о цене продукта
         "Чай черный листовой Мономах Кения 90 гр"'''
        return self.prices_parsing(
            [
                'https://eko.zakaz.ua/uk/products/chai-monomakh-90g--04820097812197/'
            ]
        )

    def arko_cool_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(
            [
                'https://atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-cool',
                'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090029/',
                'https://varus.ua/pina-dlya-golinnya-kul-arko-200ml'
            ]
        )

    def arko_sensitive_200_bonus100_parcer(self):
        '''Парсер для сбора данных о цене продукта
        "Пена для бритья ARKO Cool 300 млг+100млг бонус"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/pina-dla-golinna-200100-ml-arko-men-sensitive-promo',
                'https://eko.zakaz.ua/uk/products/pina-arko-200ml--08690506090043/',
                'https://varus.ua/pina-dlya-golinnya-ekstra-sensitiv-arko-200ml'
            ]
        )

    def carrot_parcer(self):
        '''Парсер для сбора данных о цене продукта морковь'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/morkva-1gat',
                'https://eko.zakaz.ua/uk/products/ovochi-morkva--ekomarket00000000640007/',
                'https://varus.ua/morkva-1-gatunok-vag'
            ]
        )

    def cabbage_parcer(self):
        '''Парсер для сбора данных о цене продукта капуста'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/kapusta-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-kapusta--ekomarket00000000667930/',
                'https://varus.ua/kapusta-1-gatunok-vag'
            ]
        )

    def egg_parcer(self):
        '''Парсер для сбора данных о цене продукта яйца куринные'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/ajce-kurace-10-st-ukraina-1-kategoria-fas',
                'https://eko.zakaz.ua/uk/products/iaitse--ekomarket00000026102825/',
                'https://varus.ua/yayce-kuryache-1sht'
            ]
        )

    def mayonez_detsk_shedro_67_parcer(self):
        '''Парсер для сбора данных о цене продукта "Майонез детский Щедро 67%"'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/majonez-190g-sedro-domasnij-dla-ditej-67',
                'https://eko.zakaz.ua/uk/products/maionez-shchedro-190g--04820184020054/',
                'https://varus.ua/mayonez-domashniy-dlya-ditey-67-schedro-190g-d-p-ukraina'
            ]
        )

    def rexona_aloe_vera_w_parcer(self):
        '''Парсер для сбора данных о цене продукта "Дезодорант Rexona Aloe Vera женский"'''
        return self.prices_parsing(
            [
                'https://eko.zakaz.ua/uk/products/dezodorant-reksona-150ml-velikobritaniia--08712561844338/'
            ]
        )

    def marloboro_red_parcer(self):
        '''Парсер для сбора данных о цене продукта сигареты Мальборо красные'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/sigareti-marlboro-27',
                'https://eko.zakaz.ua/uk/products/tsigarki-malboro-25g--04823003205557/',
                'https://varus.ua/cigarki-marlboro'
            ]
        )

    def beer_lvivske_svitle_24l(self):
        '''Парсер для сбора данных о цене продукта "Пиво ЛЬвовское светлое 2,4 литра"'''
        return self.prices_parsing(
            [
                'https://varus.ua/pivo-2-4l-4-5-svitle-pasteriz-lvivske'
            ]
        )

    def smetana_stolica_smaky_400_15_parcer(self):
        '''Парсер для сбора данных о цене продукта сметана "Столица Смаку 400 гр 15%"'''
        return self.prices_parsing(
            [
                'https://varus.zakaz.ua/ru/products/ukrayina--04820194043517/'
            ]
        )

    def water_in_6l_bottle_parser(self):
        '''Парсер для сбора данных о цене продукта вода питьевая в 6 литровой бутылке'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/voda-6-l-karpatska-dzerelna-negazovana',
                'https://eko.zakaz.ua/uk/products/voda-karpatska-dzherelna-6000ml--04820051240240/',
                'https://varus.ua/voda-vygoda-negazirovannaya-vygoda-6-l'
            ]
        )

    def pork_lopatka_parser(self):
        '''Парсер для сбора данных о цене продукта свинина лопатка/на кости, кг'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/okist-lembergmit-svinacij-oholodzenij-vakupak',
                'https://eko.zakaz.ua/uk/products/m-iaso--ekomarket00000000535086/',
                'https://varus.ua/lopatka-svinaya-vesovaya'
            ]
        )

    def potato_parser(self):
        '''Парсер для сбора данных о цене продукта картошка обыкновенная, кг'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/kartopla-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-kartoplia--ekomarket00000000667970/',
                'https://varus.ua/kartoplya-1-gatunok-vag'
            ]
        )

    def beet_parser(self):
        '''Парсер для сбора данных о цене продукта буряк обыкновенный, кг'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/burak-1-gat',
                'https://eko.zakaz.ua/uk/products/ovochi-buriak--ekomarket00000000646097/',
                'https://varus.ua/buryak-1-gatunok-vag'
            ]
        )

    def four_parser(self):
        '''Парсер для сбора данных о цене продукта муки, кг'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/borosno-1-kg-hutorok-psenicne-visij-gatunok',
                'https://eko.zakaz.ua/uk/products/boroshno-khutorok-1000g-ukrayina--04820101710204/',
                'https://varus.ua/boroshno-pshenichne-vigoda-1-kg'
            ]
        )

    def oil_for_dishes_parser(self):
        '''Парсер масла для приготовки блюд(самое популярное) '''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/olia-085l-olejna-tradicijna-sonasnikova-rafinovana',
                'https://eko.zakaz.ua/uk/products/oliia-oleina-850ml--04820001115567/',
                'https://varus.ua/maslo-podsolnechnoe-oleyna-tradicionnaya-rafinirovannoe-850-ml'
            ]
        )

    def sour_cream_for_dishes_parser(self):
        '''Парсер для самой популярной сметаны к блюдам (вареники, борщ, т.д.)'''
        return self.prices_parsing(
            [
                'https://www.atbmarket.com/product/smetana-300-g-agotinska-15-pstakan',
                'https://eko.zakaz.ua/uk/products/smetana-iagotin-300g--04823005209584/',
                'https://varus.ua/smetana-yagotinska-15-450g'
            ]
        )

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