import requests
from bs4 import BeautifulSoup
import json

url='https://novus.online/product/napij-gazovanij-coca-cola-15l'

headers={
     'Accept':'image/avif,image/webp,*/*',
     'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
}
# В аргументах указываем url сайта и наши заголовки:
req=requests.get(url, headers=headers)

#сохраним в переменную src полученный объект и вызовем у него метод text:
src=req.text

#распечатаем, чтобы убедиться, что мы получили код страницы:
print(src)

# 
# # #создадим ссылку на страницу сайта:
# # url='http://health-diet.ru/table_calorie/'
# #
# # #создадим заголовки, в которые добавим accept и user_agent,для того, чтобы показать сайту, что мы не бот,а человек
# headers={
#     'Accept':'*/*',
#     'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
# }
# #
# # # переменная req будет нам возвращать результат работы метода get библиотеки requests.
# # # В аргументах указываем url сайта и наши заголовки:
# # req=requests.get(url, headers=headers)
# #
# # #сохраним в переменную src полученный объект и вызовем у него метод text:
# # src=req.text
# #
# # #распечатаем, чтобы убедиться, что мы получили код страницы:
# # #print(src)
# #
# # #далее сохраним нашу страницу в файл.
# # # Т.к. многие сайты не любят, когда их парсят и велика вероятность получения бана
# # # или ограничения по времени за большое количество запросов.
# # #А сохранив страницу мы всегда можем продолжить работать с ней дальше.
# # with open('practice.html','w') as f:
# #     f.write(src)
# 
# #теперь код запроса к сайту и сохранения страницы нам не нужен, мы его закомментируем!все закомментируем, что выше!
# 
# #Далее откроем, прочитаем и сохраним наш файл страницы в переменную:
# # with open('practice.html') as f:
# #     src=f.read()
# #
# # # создадим объект BeautifulSoup и передадим ему нашу переменную src и парсер lxml  приступим к сбору данных:
# # soup=BeautifulSoup(src,'lxml')
# #
# # #исходя из нашего плана , первым делом нам нужно получить все ссылки на категории товаров
# # # найдем класс, который объединяет все товары в коде -> class='mzr-tc-group-item-href'
# # #все полученные данные мы будем сохранять в словарь!
# # #создаем пустой словарь:
# # all_categories_dict={}
# # all_products_hrefs=soup.find_all(class_='mzr-tc-group-item-href')
# # for i in all_products_hrefs:
# #     item=i.text
# #     item_href='http://health-diet.ru/' + i.get('href')  #добавим к ссылке доменное имя http://health-diet.ru/
# #     #print(f'{item} : {item_href}')  #мы получили список ссылок на продукты
# #     #запись в словарь
# #     all_categories_dict[item]=item_href
# #
# #
# #
# # #ДАЛЕЕ СОХРАНИМ НАШ СЛОВАРЬ В JSON-файл!!!!!!!!:
# # with open('all_categories_dict.json', 'w') as f:
# #     json.dump(all_categories_dict, f, indent=4, ensure_ascii=False)  #indent - отступ в нашем файле, ensure_ascii=False - не экранирует символы и помогает при работе с кириллицей
# 
# # далее закомментируем все что выше, и загружаем наш json-файл в переменную all_categories:
# with open('all_categories_dict.json') as f:
#     all_categories=json.load(f)
# 
# #распечатаем и убедимся, что в этой переменной находится словарь
# #print(all_categories)
# 
# #далее создадим цикл, на каждой итерации которого мы будем заходить на новую страницу категории,
# # собирать из нее все данные о товарах и их химическом составе и записывать все это в файл:
# count=0
# for category_name, category_href in all_categories.items():
#     #каждую страницу будем сохранять под именем категории,мы решили что запятую,дейис и пробел в именах мы заменим на нижний слэш для читабельности
#     # создадим список из символов, которые хотим заменить
#     if count==0:
#         rep=[',', ' ', '-',"'"]
#         #затем в цикле пробежимся по нашим символам:
#         for item in rep:
#             #пишем условие, что если символ есть в имени, то меняем его на нижний слэш
#             if item in category_name:
#                 category_name=category_name.replace(item,'_')
#         #print(category_name)
# 
#         #далее переходим к запросам на странице. Раскомментируем заголовки, чтобы мы могли их снова использовать
#         req=requests.get(url=category_href, headers=headers)
# 
#         #сохраняем результат в переменную src
#         src=req.text
# 
#         #и сохраним каждую нашу html страницу под именем категории в папку data
#         with open(f'data/{count}_{category_name}.html','w') as f:
#             f.write(src)
# 
#         count+=1

