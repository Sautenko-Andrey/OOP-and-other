def kogda_chaus_vihodnoy():
    """
    Необходимо написать программу, которая будет показывать
     по каким дням Саша выходной, в зависимости от входных данных ( в каких
    числах он уже работает( Чаус раюотате 2 через 2 ).
    :return: None
    """
    #kind_of_mounth=int(input("Введи сколько дней в заданном месяце: 27,30 или 31 ? "))
    name_month=input("Какой месяц интересует? ")
    monday='Понедельник'
    thuesday="Вторник"
    wednesday="Среда"
    thursday="Четверг"
    friday="Пятница"
    saturday="Суббота"
    sunday="Воскресенье"
    kalendar=[1,2,3,4,5,6,7,8,9,10,
              11,12,13,14,15,16,17,18,19,20,
              21,22,23,24,25,26,27,28,29,30,31
    ]
    for days in range(1):
        if name_month=="Февраль":
            kalendar=kalendar[0:-3]
            for days in kalendar:
                if days==1 or days==8 or days==15 or days==22:
                    print(days,"февраля","-",monday)
                if days==2 or days==9 or days==16 or days==23:
                    print(days,"февраля","-",thuesday)
                if days==3 or days==10 or days==17 or days==24:
                    print(days,"февраля","-",wednesday)
                if days==4 or days==11 or days==18 or days==25:
                    print(days,"февраля","-",thursday)
                if days==5 or days==12 or days==19 or days==26:
                    print(days,"февраля","-",friday)
                if days==6 or days==13 or days==20 or days==27:
                    print(days,"февраля","-",saturday)
                if days==7 or days==14 or days==21 or days==28:
                    print(days,"февраля","-",sunday)
        elif name_month=="Апрель":
            kalendar.pop()
            for days in kalendar:
                if days==5 or days==12 or days==19 or days==26:
                    print(days,"апреля","-",monday)
                if days==6 or days==13 or days==20 or days==27:
                    print(days,"апреля","-",thuesday)
                if days==7 or days==14 or days==21 or days==28:
                    print(days,"апреля","-",wednesday)
                if days==1 or days==8 or days==15 or days==22 or days==29:
                    print(days,"апреля","-",thursday)
                if days==2 or days==9 or days==16 or days==23 or days==30:
                    print(days,"апреля","-",friday)
                if days==3 or days==10 or days==17 or days==24:
                    print(days,"апреля","-",saturday)
                if days==4 or days==11 or days==18 or days==25:
                    print(days,"апреля","-",sunday)
        elif name_month == "Июнь":
            kalendar.pop()
            for days in kalendar:
                if days == 7 or days == 14 or days == 21 or days == 28:
                    print(days, "июня", "-", monday)
                if days == 1 or days == 8 or days == 15 or days == 22 or days == 29:
                    print(days, "июня", "-", thuesday)
                if days == 2 or days == 9 or days == 16 or days == 23 or days == 30:
                    print(days, "июня", "-", wednesday)
                if days == 3 or days == 10 or days == 17 or days == 24:
                    print(days, "июня", "-", thursday)
                if days == 4 or days == 11 or days == 18 or days == 25:
                    print(days, "июня", "-", friday)
                if days == 5 or days == 12 or days == 19 or days == 26:
                    print(days, "июня", "-", saturday)
                if days == 6 or days == 13 or days == 20 or days == 27:
                    print(days, "июня", "-", sunday)
        elif name_month == "Сентябрь":
            kalendar.pop()
            for days in kalendar:
                if days == 6 or days == 13 or days == 20 or days == 27:
                    print(days, "сентября", "-", monday)
                if days == 7 or days == 14 or days == 21 or days == 28:
                    print(days, "сентября", "-", thuesday)
                if days == 1 or days == 8 or days == 15 or days == 22 or days == 29:
                    print(days, "сентября", "-", wednesday)
                if days == 2 or days == 9 or days == 16 or days == 23 or days == 30:
                    print(days, "сентября", "-", thursday)
                if days == 3 or days == 10 or days == 17 or days == 24:
                    print(days, "сентября", "-", friday)
                if days == 4 or days == 11 or days == 18 or days == 25:
                    print(days, "сентября", "-", saturday)
                if days == 5 or days == 12 or days == 19 or days == 26:
                    print(days, "сентября", "-", sunday)
                #or name_month=="Ноябрь":
        else:
            print(name_month,kalendar)
        #отсортировал количество дней в зависимости от месяца года.
        #далее нужно придумать как привязать числа к дням недели в зависимости от месяца
        #далее придумать как привязать входное число ,когда чаус вышел на работу +1 день
#нам нужно два параметра функции на входе(в качестве аргументов)-это месяц и число(2 числа?)
kogda_chaus_vihodnoy()