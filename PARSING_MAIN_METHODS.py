import re
import requests
from bs4 import BeautifulSoup
import json

url='https://auchan.zakaz.ua/ru/products/pivo-obolon-1000ml-ukrayina--04820193032413/'
headers={
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'
        }
req=requests.get(url,headers=headers)
src=req.text
print(src)

# далее сохраним нашу страницу в файл.
# Т.к. многие сайты не любят, когда их парсят и велика вероятность получения бана
# или ограничения по времени за большое количество запросов.
# А сохранив страницу мы всегда можем продолжить работать с ней дальше.
with open('products_data/obolon_premium_(1.1).html','w') as f:
     f.write(src)

#Далее откроем, прочитаем и сохраним наш файл страницы в переменную:
with open('products_data/obolon_premium_(1.1).html') as f:
     src=f.read()

soup=BeautifulSoup(src,'html.parser')
obolon_price_silpo=soup.find(class_='jsx-161433026 Price__value_title').text
print(obolon_price_silpo)
# with open('/home/andrey/Загрузки/obolon.html') as f:
#     src=f.read()
# #print(src)
# soup=BeautifulSoup(src,'html.parser')
# #найдем цену пива оболонь:
# obolon_price=soup.find(class_='jsx-161433026 Price__value_title').find_next().text
# print(f'{obolon_price} грн')

#
#print(src)
#аем объект BeautifulSoup, чтобы обращаться к нему и извлекать нужные данные:
#soup=BeautifulSoup(src,'html.parser')

# # к примеру получим иформацию из тега title нашей страницы сайта:
# title=soup.title
#print(title)
#чтобы получить содержимое тега нужно использовать метод text:
#print(title.text)
#либо использовать метод string:
#print(title.string)

#Рассмотрим работу с методами find() и find_all(), которые решают многие задачи парсинга:
# Эти методы работают на странице сверху вниз.
# К примеру на странице у нас есть несколько тегов h6.
# Если мы выозовем метод find, то увидим, что мы забрали данные из первого попавшегося ему заголовка h6:
# page_h6=soup.find('h6')
# print(page_h6.text)
# print()

# а метод  find_all() заберет всю инфу из каждого тега h6 и сохранит ее в список:
# page_all_h6=soup.find_all('h6')
# print(page_all_h6)
# print()
# # этот список мы можем перебрать в цикле:
# for i in page_all_h6:
#     print(i.text)

# помимо поиска по тегу мы можем конкретизировать наш запрос указывая атрибут тега:
# например получим запись кнопки ФОТО из index2.
# Лежит оно в теге h4 внутри тега div с классом "col-xl-4 col-md-12 col-sm-12"
# buttom_foto=soup.find('div', class_="col-xl-4 col-md-12 col-sm-12")
# print(buttom_foto.text.strip())   #strip для обрезки пробелов

#мы так же можем продолжить связку слов шагая в глубь по коду.
# Мы указываем весь путь к нужному тегу.
# например возьмем {{info.title}} :
# info_title=soup.find('div',class_='container').find(class_='row').find(class_="col-xl-12 col-md-12 col-sm-12" ).find('h1')
# print(info_title.text)

#вторым способом задания атрибутов для фильтрации поиска,
# вместо того, чо делалось выше, является передача словаря,
# в котором в качестве пар ключ-значение мы указываем параметры отбора.
# Также через запятую в словаре мы можем указыать дополнительные параметры отбора, такие как id к примеру.
# в этом примере доп.параметры не указываются
# info_title=soup.find('div',{'class':'container'}).find('div',{'class':'col-xl-12 col-md-12 col-sm-12'}).find('h1').text
# print(info_title)

# #далее практикуюсь с методом find_all().Соберу все теги <li> из <ul> класса "dropdown-menu"
# all_li_in_ull_dropdown_menu=soup.find(class_="dropdown-menu").find_all('li')
# print(all_li_in_ull_dropdown_menu, len(all_li_in_ull_dropdown_menu), sep='\n')
# print()
# #пройдемся по этому списку циклом:
# for i in all_li_in_ull_dropdown_menu:
#     print(i.text)
# print()
#
# #т.к. это список, мы мы можем обращаться к каждому эл-ту по индексу:
# #к примеру выведем третью запись из списка:
# third_item=all_li_in_ull_dropdown_menu[2]
# print(f'Третья запись в списке: {third_item.text}')

#продолжаем практику с find() , find_all(). Для примера спарсим все названия магазинов
# all_markets=soup.find(class_='container2').find_all('button')
# for i in all_markets:
#     print(i.text.split())

#второй способ еще проще!Вместо того,
# чтобы пробегаться по тегам в глубину, указав просто все кнопки button
# all_markets=soup.find_all('button')
# print(all_markets)
# for i in all_markets:
#     print(i.text.split())
#
# # спарсим ссылки для ПО ФОТО и ПО НАЗВАНИЮ:
# all_links=soup.find_all('div',class_='container')
# res=all_links[1]
# all_links=soup.find_all('div',class_='col-xl-4 col-md-12 col-sm-12')
# result=all_links[1]
# all_links=soup.find_all('a')
# for i in all_links:
#     item_url=i.get('href')
#     print(item_url)

# #или вот так. возьмем все теги a и заберем только первые два:
# all_a=soup.find_all('a')
# we_need=all_a[:2]
# for i in we_need:
#     item_text=i.text
#     item_url=i.get('href')     #можно также вместо get писать ключ ['href'] вот так item_url=i['href]
#     print(f'{item_text} : {item_url}')

# ДЛЯ перемещения по дом-дереву есть несколько полезных методов.
# Рассмотрим методы  find_parent() и find_parents().
# Эти методы ищут родителя или родителей элементов.
# Т.е. поднимаются по структуре html-дерева снизу-вврех
# и их действия аналогичны методам find(),find_all() c одной поправкой,
# что мы используем их когда нужно подниматься вверх, ане опускаться в глубь кода
# найдем родителя для {{info.under_title}}
# res=soup.find('h6').find_parent()
# print(res)

#а метод find_parents  поднимается до самого верха, включая и body и html-тег
# res=soup.find('h6').find_parents()
# print(res)

# ЕЩЕ одними полезными методами для перемещения по коду являются next_element() и previous_element()
# next - двигается пошагово и возвращает следущий элемент в коде.
# К примеру спарсим <b><img src="{% static 'my_app/images/ATB.png' %}"> АТБ</b>
#иногда надо дублировать подряд метод next_element() из-за отступов
# res=soup.find(class_='btn-group').next_element()
# print(res)
#так же есть похожий на него метод find_next(),
# а  метод previous_element является полной противоположностью этим двум методам.


#РАссмторим методы find_next_sibling() и find_previous_sibling().
# Они возвращают следующие и предыдущие элементы внутри искомого тега:
# res=soup.find(class_='container').find_next_sibling().find_next_sibling()
# print(res)

#find_previous_sibling() - работает совершенно противоположно
# res=soup.find(class_='container2').find_previous_sibling().find_previous_sibling()
# print(res)
#МЫ МОЖЕМ КОМБИНИРОВАТЬ все эти методы:
# res=soup.find(class_='container2').find_previous_sibling().find_previous_sibling().find_next().find_next().find_next().text
# print(res)

#КОМБИНАЦИИ МЕТОДОВ ДАЮТ НАМ НЕОГРАНИЧЕННЫЕ ВОЗМОЖНОСТИ ПАРСИНГА КОГДА И ПЕРЕМЕЩЕНИЯ ПО СТРАНИЦЕ!!!
#

#мы можем искать элементы передавая в параметр текст.
# Попробуем найти ссылку с текстом ПО НАЗВАНИЮ
# find_a_by_text=soup.find('a',text='ПО ФОТО').text   # !!!осуществляется поиск по полному содержанию!!!
# print(find_a_by_text)

# ЭТО может стать проблемой, если мы ищем по большому тексту! => <h6>Выберите способ поиска товара :</h6>
# Чтобы решить эту задачу, испозуем регулярные выражения re
# res=soup.find('h6',text=re.compile('Выберите')).text
# print(res)

# а что если нам нужно собрать всеблоки, в которых содержится слово "Цена"?
# find_all_prices=soup.find_all(text=re.compile('([Цц]ена)')) # чтобы искал и с маленькой и с заглавной буквой слова Цена
# print(find_all_prices)