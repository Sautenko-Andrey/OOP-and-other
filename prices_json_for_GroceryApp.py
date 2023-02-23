import json
from selenium_python.chrome_driver.PARSERS_FOR_ALL import ProductParserVol2

# with open('prices_store.json') as f:
#     store=json.load(f)
#
# # print(store)
# # print(type(store))
# # marlboro_red=store['products']['marlboro_red']
# # print(f'Цены сигарет Мальборо : {marlboro_red["atb"],marlboro_red["eko"], marlboro_red["varus"]}')
# for item, value in store.items():
#     for product,price in value.items():
#         print(product)
#         print(price)
#         print('-------------------------------------------------')

#запись в json (обновление полностью всего файла с продуктами)
# product='Marlboro RED'
# prices={"atb":77.00,"eko":79.00,"varus":81.00}
# product2='Vodka'
# prices2={"atb":1000.00,"eko":100.00,"varus":333.00}
# to_json={product:prices,product2:prices2}
#
# with open('prices_store.json','w') as f:
#     json.dump(to_json, f)

parser=ProductParserVol2()

all_products_names=[
    {'obolon_premium_1.1_l':{
    "atb":parser.obolon_premium_parser()[0],
    "eko":parser.obolon_premium_parser()[1]
}},
    {'vodka_hetman_ice_07':{
        "atb":parser.vodka_getman_ICE_parcer()[0]
}},
    {'coca_cola_2l':{
        "atb":parser.coca_cola_2l_parcer()[0],
        "eko":parser.coca_cola_2l_parcer()[1],
        "varus":parser.coca_cola_2l_parcer()[2],
        "silpo":parser.coca_cola_2l_parcer()[3],
        "ashan":parser.coca_cola_2l_parcer()[4]
}},
    {'garlik':{
        "atb":parser.garlik_parcer()[0],
        "eko":parser.garlik_parcer()[1],
        "varus":parser.garlik_parcer()[2],
        "silpo":parser.garlik_parcer()[3]
}},
    {'tea_minutka':{
        "atb":parser.tea_minutka_black_40_b_parcer()[0],
        "eko":parser.tea_minutka_black_40_b_parcer()[1]
}},
    {'apple_golden':{
        "atb":parser.apple_golden_parcer()[0],
        "eko":parser.apple_golden_parcer()[1],
        "varus":parser.apple_golden_parcer()[2],
        "silpo":parser.apple_golden_parcer()[3]
}},
    {'sigarets_kent_8':{
        "atb":parser.kent_8_parcer()[0],
        "eko":parser.kent_8_parcer()[1],
        "varus":parser.kent_8_parcer()[2],
        "silpo":parser.kent_8_parcer()[3]
}},
    {'coffee_aroma_gold':{
        "eko":parser.coffee_aroma_gold_parcer()[1]
}},
    {'oil_shedriy_dar_raf_850':{
        "atb":parser.oil_shedriy_dar_850_parcer()[0],
        "eko":parser.oil_shedriy_dar_850_parcer()[1],
        "varus":parser.oil_shedriy_dar_850_parcer()[2],
        "silpo":parser.oil_shedriy_dar_850_parcer()[3]
}},
    {'fairy_limon_500':{
        "atb":parser.fairy_limon_500_parcer()[0],
        "eko":parser.fairy_limon_500_parcer()[1],
        "varus":parser.fairy_limon_500_parcer()[2],
        "silpo":parser.fairy_limon_500_parcer()[3]
}},
    {'onion':{
        "atb":parser.onion_parcer()[0],
        "eko":parser.onion_parcer()[1],
        "varus":parser.onion_parcer()[2],
        "silpo":parser.onion_parcer()[3]
}},
    {'apple_black_prince':{
        "atb":parser.apple_black_prince_parcer()[0],
        "eko":parser.apple_black_prince_parcer()[1],
        "varus":parser.apple_black_prince_parcer()[2],
        "silpo":parser.apple_black_prince_parcer()[3]
}},
    {'smetana_stol_smaky_20%':{
        "varus":parser.smetana_stolica_smaky_400_20()[2]
}},
    {'limon':{
        "atb":parser.limon_parcer()[0],
        "eko":parser.limon_parcer()[1],
        "varus":parser.limon_parcer()[2],
        "silpo":parser.limon_parcer()[3]
}},
    {'oil_oleyna_neraf_850':{
        "eko":parser.oil_oleyna_neraf_850_parcer()[1]
}},
    {'tea_monomah_kenya_90':{
        "eko":parser.tea_monomah_black_kenya_90_parcer()[1]
}},
    {'arko_cool_200':{
        "atb":parser.arko_cool_200_bonus100_parcer()[0],
        "eko":parser.arko_cool_200_bonus100_parcer()[1],
        "varus":parser.arko_cool_200_bonus100_parcer()[2],
        "silpo":parser.arko_cool_200_bonus100_parcer()[3]
}},
    {'arko_sensitive_200':{
        "atb":parser.arko_sensitive_200_bonus100_parcer()[0],
        "eko":parser.arko_sensitive_200_bonus100_parcer()[1],
        "varus":parser.arko_sensitive_200_bonus100_parcer()[2],
        "silpo":parser.arko_sensitive_200_bonus100_parcer()[3]
}},
    {'carrot':{
        "atb":parser.carrot_parcer()[0],
        "eko":parser.carrot_parcer()[1],
        "varus":parser.carrot_parcer()[2],
        "silpo":parser.carrot_parcer()[3]
}},
    {'cabbage':{
        "atb":parser.cabbage_parcer()[0],
        "eko":parser.cabbage_parcer()[1],
        "varus":parser.cabbage_parcer()[2],
        "silpo":parser.cabbage_parcer()[3]
}},
    {'eggs':{
        "atb":parser.egg_parcer()[0],
        "eko":parser.egg_parcer()[1],
        "varus":parser.egg_parcer()[2],
        "silpo":parser.egg_parcer()[3]
}},
    {'mayonez_detsk_shedro_67%':{
        "atb":parser.mayonez_detsk_shedro_67_parcer()[0],
        "eko":parser.mayonez_detsk_shedro_67_parcer()[1],
        "varus":parser.mayonez_detsk_shedro_67_parcer()[2],
        "silpo":parser.mayonez_detsk_shedro_67_parcer()[3]
}},
    {'rexona_aloe_vera':{
        "eko":parser.rexona_aloe_vera_w_parcer()[1]
}},
    {'marlboro_red':{
        "atb":parser.marloboro_red_parcer()[0],
        "eko":parser.marloboro_red_parcer()[1],
        "varus":parser.marloboro_red_parcer()[2],
        "silpo":parser.marloboro_red_parcer()[3],
        "ashan":parser.marloboro_red_parcer()[4]
}},
    {'beer_lvivske_svetl_2.4 l':{
        "varus":parser.beer_lvivske_svitle_24l()[2],
        "silpo":parser.beer_lvivske_svitle_24l()[3]
}},
    {'smetana_stol_smaky_15%':{
        "varus":parser.smetana_stolica_smaky_400_15_parcer()[2]
}},
    {'water_in_bottle_6l':{
        "atb":parser.water_in_6l_bottle_parser()[0],
        "eko":parser.water_in_6l_bottle_parser()[1],
        "varus":parser.water_in_6l_bottle_parser()[2]
}},
    {'pork_lopatka':{
        "atb":parser.pork_lopatka_parser()[0],
        "eko":parser.pork_lopatka_parser()[1],
        "varus":parser.pork_lopatka_parser()[2]
}},
    {'potato':{
        "atb":parser.potato_parser()[0],
        "eko":parser.potato_parser()[1],
        "varus":parser.potato_parser()[2]
}},
    {'beet':{
        "atb":parser.beet_parser()[0],
        "eko":parser.beet_parser()[1],
        "varus":parser.beet_parser()[2],
        "silpo":parser.beet_parser()[3],
}},
    {'four':{
        "atb":parser.four_parser()[0],
        "eko":parser.four_parser()[1],
        "varus":parser.four_parser()[2]
}},
    {'oil_for_dish':{
        "atb":parser.oil_for_dishes_parser()[0],
        "eko":parser.oil_for_dishes_parser()[1],
        "varus":parser.oil_for_dishes_parser()[2]
}},
    {'smetana_for_dish':{
        "atb":parser.sour_cream_for_dishes_parser()[0],
        "eko":parser.sour_cream_for_dishes_parser()[1],
        "varus":parser.sour_cream_for_dishes_parser()[2]
}},
    {'desodorant_garnier_man':{
        "silpo":parser.desodorant_garnier_magniy_man_parser()[3]
    }}]

def get_all_prices():
    to_json=dict()
    for item in all_products_names:
        for product,values in item.items():
            print(f'Заносим {product} в базу данных.....')
            to_json[product]=values
            print('Ждем.........')
    with open('prices_store3.json','w') as f:
        json.dump(to_json, f, sort_keys=False, indent=len(all_products_names))
        print('Сделано!')

get_all_prices()



# product_names=['marlboro red','kent 8', 'beer obolon']
# prices=[{'obolon':{"atb":77.00,"eko":79.00,"varus":81.00}},{"atb":1000.00,"eko":100.00,"varus":333.00},{"atb":obolon_atb}]
# def get_prices():
#     to_json=dict()
#     i=0
#     for item in product_names:
#         to_json[item]=prices[i]
#         i+=1
#     print(to_json)
#     with open('prices_store2.json','w') as f:
#          json.dump(to_json, f, sort_keys=False, indent=3)






