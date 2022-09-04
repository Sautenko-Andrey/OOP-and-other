import re

def main1():
    text='Everyboy loves footballgame. Football is most fabulous game in the world!'

    result=re.findall(r'\bgame\b',text)

    text2='Мало мясо, надо сало, потому что его никогда не бывает мало!'
    result2=re.findall(r'ало',text2)

    print(result)
    print(result2)

    text3='(кал), каловейчик,калоквиум.'
    result3=re.findall(r'\(кал\)',text3)
    print(result3)

    text4='Еда, еду, победа'
    result4=re.findall(r'[Ее]д[уа]',text4)
    print(result4)

    text5='Барсик, барсик, барсику, барсика'
    result5=re.findall(r'[Бб]арсик[уа]',text5)
    print(result5)

    text6='i have bought 5 beers.'
    result6=re.findall(r'[0-9]',text6)
    print(result6)

    print(re.findall(r'[0-9][0-9]','i have bought 77 beers.'))

    print(re.findall(r'[-0-9][0-9]','Today we have frost -5 and in 30 days it will fall down.'))

    print(re.findall(r'[^0-9]','I would like to dump you after 3 years relationships.'))

    print(re.findall(r'[оса]','Я купил самосвал'))

    print(re.findall(r'[^лох]','Данил просто лох!'))

    print(re.findall(r'[а-яА-Я0-9]','Я ищу работу программиста за 3000 евро в месяц!'))

    print(re.findall(r'\d','i am 32 y.o'))
    print(re.findall(r'.','I am gonna departure from Ukraine in 5 weeks'))
    print(re.findall(r'\w','Where i can enjoy waxing in 5 minutes?'))
    print(re.findall(r'0x[\da-fA-F]','0xf,0xa,0x5'))


#main1()

                                                 #КВАНТИФИКАТОРЫ
def main2():
    text='Google, gooogle, goooole'
    result=re.findall(r'o{2,5}',text)
    print(result)
    print(re.findall(r'o{2,5}?','google, gooogle,goooooole'))
    print(re.findall(r'[Gg]o{2,}gle','Google,Gooogle,goooooogle'))
    print(re.findall(r'[gG]o{,4}gle','Google,gooogle,goooooogle'))
    print(re.findall(r'8\d{10}','80950180611'))
    print(re.findall(r'8050\d{6}','8050666412'))
    print(re.findall(r'a{2,4}?','andrey,aaaaalla,aaron'))
    print(re.findall(r'aa?ron','aaron,aron'))

    print(re.findall(r'[gG]o{2,5}gle','google,gooogle,goooooogle'))

    print(re.findall(r'o{2,5}', 'gogle,google,goooogle,goooooogle'))
    print(re.findall(r'o{2,5}?','gogle,google,gooogle,goooogle,gooooogle'))

    print(re.findall(r'max{3}','maxxxxxxxxx'))
    print(re.findall(r'salo\d{5}','salo12345'))
    print(re.findall(r'ann?a','ana,anna'))

    text77='Игрок-Саутенко А.Е.; рост-192 см; город-Краматорск'
    result77=re.findall(r'\w+\s*-\s*[^;]+',text77)
    print(result77)
    print(re.findall(r'\w+-\w+,\w+-[^;]+','player-Chasov,city-Kramatorsk; player2-Sautenko,city-Kramatorsk'))
    print(re.findall(r'(\w+)\s*([^;]+)','city Kramatorsk; city Slovyansk; city Svyatogorsk'))
    print(re.findall(r'\w+\s*\w+\s*[^,]+','igor plays football, alex plays volleyball, andrey is developer'))

    print(re.findall(r'<img\s+src\s*[^>]+>','<p>Картинка<img src="some.com"> в тексте<\p>'))
    print(re.findall(r'"\w+"','I am gonna drink only beer which names "Hike"!'))



                                          #СОХРАНЯЮЩИЕ СКОБКИ И ГРУППИРОВКА

    print(re.findall(r'(?:let|lon)\s*=\d+','let=5,lon=7,a=33'))
    print(re.findall(r'(?:weight|height)\s*=\d+','weight=90,height=202,name=Alex,phone=0956874521')) #несохраняющие скобки
    print(re.findall(r'(name|surname)\s*=(\w+)','name=Andrey,surname=Sautenko,id=86484684'))  #сохраняющие скобки
    print(re.findall(r'(club|city)\s*-\s*(?:\w+)','club-Arsenal,city-London,colour-red'))  #сохраняются только ключи


                                                      #ПРОВЕРКИ И ФЛАГИ
    print(re.findall(r'прибыль|обретение|доход','Подоходный налог')) #не обращать на это внимание!это просто типа пример

    print(re.findall(r'прибыль|обретение|\bдоход\b', 'Подоходный налог,доход')) #неоптимальный вариант
    print(re.findall(r'\b(прибыль|доход|приход)\b','Он заплатил подоходный налог, и не получил прибыль'))

    #примеры использования

    text99="""
    <!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>{% block title %}Блок заголовка{% endblock %}</title>
</head>
<body>

{% block content %}
	{% block table_contents %}
	<ul>
	{% for i in list_table -%}
	<li>{% block item scoped %}{{ i }}{% endblock %}</li>
	{% endfor %}
	</ul>
	{% endblock table_contents %}
{% endblock %}

</body>
</html>
    """
#из этого текста мы хотим выделить содержимое тега <body>
    result=re.findall(r'^<body.*?>([\w\W]+)(?=</body>)',text99,re.MULTILINE)
    print(result)






main2()
