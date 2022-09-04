#                 ЧЕРНОВОЙ ВАРИАНТ ПРОГРАММЫ ДЛЯ ПОВТОРЕНИЯ СЛОВ НА АНГЛИЙСКОМ ЯЗЫКЕ!
import pickle
def main():
    """
    Программа принимает и сохраняет новые английские слова в словарь.
    :return: None
    """
    #создадим словарь,куда будем сохранять слово/перевод и запишем в файл.
    file=open('D:\Фильмы\my_vocabulary3.dat', 'wb')
    vocabulary={'ШТУКИ/ТЫСЯЧИ/ГРАНД':'GRAND','СТАВКА/КУРС/КОЕФИЦИЕННТ':'RATE','УСИЛИТЬ/АКТИВИЗИРОВАТЬ':'TO STEP UP',
                'ВРАЖДЕБНОСТЬ':'HOSTILITY','ХАМСТВО':'RUDENESS','ВЯЛЫЙ':'FLACCID','ВЫПЕЧКА':'PASTRY',
                'ТЫ РАЗЫГРЫВАЕШЬ МЕНЯ?':'ARE YOU SHITTING ME?','ПРЯМАЯ ЗАВИСИМОСТЬ':'LINEAR CORRELATION',
                'КОНТРОЛЬНЫЕ ПОКАЗАТЕЛИ':'BENCHMARKS','НЕОБХОДИМЫЙ/СООТВЕТСТВУЮЩИЙ':'RELEVANT','ПРОЦВЕТАТЬ':'TO THRIVE',
                'ПОДСЧИТАТЬ/ОПРЕДЕЛИТЬ КОЛИЧЕСТВО':'TO QUANTIFY','НЕРЕШИТЕЛЬНЫЙ':'HESITANT','ПРОИЗВОДИТЬ':'TO MANUFACTURE',
                'НАПРЯЖЕНИЕ/НАПРЯЖЕННОСТЬ':'TENSION','ПОИСК ДАННЫХ':'DATA RETRIEVAL', 'ОПТОВОЛОКОННЫЙ':'FIBER-OPTIC',
                'ВЗАИМОДЕЙСТВИЕ/СИНЕРГИЯ':'SYNERGY','СВОРАЧИВАТЬСЯ/ЗАКРУГЛЯТЬСЯ':'TO WRAP THIS UP','ТАЙНА/ЗАГАДКА':'MYSTERY',
                'НЕИЗМЕРЯЕМЫЙ':'UNMEASURED','ПРОЦВЕТАНИЕ/БЛАГОПОЛУЧИЕ':'PROSPERITY','НАЗНАЧАТЬ':'TO DESIGNATE',
                'ВЫБИТЬ/ВЫРУБИТЬ(ПР.ВЫРУБИТЬ ЭЛЕКТРИЧЕСТВО)':'TO KNOCK OUT','КВАРТАЛЬНЫЙ':'QUARTERLY','ПРОГНОЗЫ':'PROJECTIONS',
                'ВРАЩЕНИЕ':'SPIN','ТЫ МОЖЕШЬ РАССЧИТЫВАТЬ НА МЕНЯ!':'YOU CAN COUNT ON ME!','КОШЕРНАЯ ЕДА':'KOSHER MEAL',
                'АКЦИОНЕР':'SHAREHOLDER','ИДЕИ/СООБРАЖЕНИЯ':'INSIGHTS','РАЗВРАЩАТЬ/ИЗВРАЩАТЬ':'TO PERVERT',
                'РАСЧЕТ/ПОДСЧЕТ':'ESTIMATION','МНЕ КАЖЕТСЯ...':'METHINKS','КОПАТЬ':'TO DIG','ДЖАКУЗИ':'HOT TUB',
                'КОПЫТА':'HOOVES','ВЫХОДНОЕ ПОСОБИЕ':'SEVERANCE','ФИНАНСОВЫЙ ДИРЕКТОР':'CFO','ПРЕДЪЯВИТЬ ОБВИНЕНИЕ':'TO INDICT',
                'ГЕНЕРАЛЬНЫЙ ДИРЕКТОР':'CEO','ЖЕРТВЫ/ЖЕРТВОПРИНОШЕНИЯ':'SACRIFICES','В СЛЕДУЮЩИЙ РАЗ':'RAIN CHECK!',
                'ДАЙ ПЯТЬ!':'UP HIGH!','ЛУЖАЙКА/ГАЗОН':'LAWN','ИЗЫМАТЬ(ЗА НЕУПЛАТУ)':'TO REPOSSESS','ПЕНСИЯ':'PENSION',
                'ПОХОРОНЫ':'FUNERAL','НЕУВАЖИТЕЛЬНО':'DISRESPECTFUL','ПОЛОВОЕ СОЗРЕВАНИЕ':'PUBERTY','ОТОЙДИ!':'BACK AWAY!',
                'МНЕ СТЫДНО!':'I AM ASHAMED!','ПРЕДСТАВЛЯТЬ(ЧЬИ-ТО ИНТЕРЕСЫ)':'TO REPRESENT','ПРЕДАННОСТЬ':'DEVOTION',
                'СКЛОНИТЬ/ПОКЛОНИТЬСЯ':'TO BOW','ВОЗДУШНЫЙ ЗМЕЙ':'KITE','СЛИШКОМ':'OVERLY','ВИЛКА':'FORK',
                'МОТЫЛЬКИ/МОЛЬ':'MOTHS','КАЧЕЛИ':'PORCH SWING','ПЬЯНЫЙ':'WASTED','МЯСНОЙ РУЛЕТ':'MEAT LOAF',
                'КРАН/СМЕСИТЕЛЬ':'FAUCET','ВОДА ИЗ-ПОД КРАНА':'TAP WATER','РАСПРОСТРАНЕНИЕ':'SPREAD','РАЗВЕЯТЬ':'TO SCATTER',
                'ИЗОБРАЖАТЬ':'TO DEPICT','ЧИСТИТЬ(ПР.ОТ КОЖУРЫ БАНАН)':'TO PEEL','СКОРЕЕ':'RATHER','ЖЕЛУДИ':'ACORNS',
                'ХЛОПЬЯ':'CEREAL', 'СВЕЧИ ЗАЖИГАНИЯ':'SPARK PLUGS', 'СМЕНА':'SHIFT', 'ПРОКЛАДКА/САЛЬНИК':'GASKET',
                'ЛОСОСЬ':'SALMON','БЕСПОРЯДОК':'MESS', 'ПЕРЕХОДНИК':'ADAPTER','АККУРАТНО/ОПРЯТНО':'NEATLY',
                'ОГРОМНЫЕ ДЕНЬГИ/СОСТОЯНИЕ':'FORTUNE','БАГАЖ':'LUGGAGE','ПРИНЦИП ЕДИНСТВЕННОЙ ОТВЕТСТВЕННОСТИ':'SINGLE RESPONSIBILITY PRINCIPLE',
                'ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ':'OPEN-CLOSED PRINCIPLE','ПРИНЦИП ПОДСТАНОВКИ ЛИСКОВ':'LISKOV SUBSTITUTION PRINCIPLE',
                'ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСА':'INTERFACE SEGREGATION PRINCIPLE','ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ':'DEPENDENCY INVERSION PRINCIPLE',
                'ЛЕСТНИЦА':'LADDER','УЕБАНСКИЙ/УЕБИЩЕ':'FUGLY','СОПЛИВЫЙ':'SNOTTY', 'РУК ДЕЛО':'HANDIWORK',
                'СКОВОРОДКА':'FRYING PAN','ЛОТЕРЕЯ':'RAFFLE','ПРИЕМНАЯ СЕМЬЯ':'FOSTER FAMILY','ПРИТВОРЯТЬСЯ':'TO PRETEND',
                'ЛАСТЫ':'FLIPPERS','СЧАСТЛИВАЯ СЛУЧАЙНОСТЬ':'FLUKE','ЛЫСЫЙ':'BALD','ХВАТИТ НЕСТИ ЧУШЬ!':'CUT THE CRAP!',
                'ДРЯХЛЫЙ/МОРЩИНИСТЫЙ':'WRINKLY','МЕРЗОСТЬ/ГАДОСТЬ':'GROSS','ФАЛЬШИВЫЙ':'BOGUS','ГОРЧИЦА':'MUSTARD',
                'ВОСХОЖДЕНИЕ':'ASCENT','ЗАЯВЛЕНИЕ':'STATEMENT','УНАСЛЕДОВАТЬ':'TO INHERIT','ФАРТУК':'APRON',
                'ОБМАНУТЬ':'TO TRICK','СКРИПКА':'FIDDLE','БОЛЬНОЕ ГОРЛО':'STREP THROAT','ОБВИСАТЬ':'TO SAG',
                'МУСОРНЫЙ БАК':'DUMPSTER','НАСЛЕДНИК':'HEIR','ПОДКРАДАТЬСЯ':'TO SNUCK UP','МЕШОК':'SACK',
                'МЯСНИК':'BUTCHER','РЕМОНТ':'REPAIR','ГРЕТЬСЯ':'TO BASK','ВЗНОС/ВКЛАД':'CONTRIBUTION','ВЕРАНДА':'PORCH',
                'СТРАННО/СТРАННЫЙ':'ODD','ЗАГАР':'TAN','ТРУП':'CORPSE','ЭГОИЗМ':'SELFISHNESS','ИГЛА':'NEEDLE',
                'БОГОСЛУЖЕНИЕ':'WORSHIP','Я ПОТРЯСЕН!':'I AM STUNNED!','СОЖИТЕЛЬСТВОВАТЬ':'TO SHACK UP',
                'ФОРЕЛЬ':'TROUT','ИСКРЕННИЙ':'SINCERE','ПИТОМНИК':'KENNEL','ВПАДАТЬ В СПЯЧКУ':'TO HIBERNATE',
                'ПОТОМ/ПОСЛЕ':'AFTERWARDS','РАЗВЕДКА':'RECON','НОВОСЕЛЬЕ':'HOUSEWARMING','ВРЕД/УЩЕРБ':'HARM',
                'ОБИДА':'RESENTMENT','НАОБОРОТ':'CONVERSELY','НЕВЫНОСИМЫЙ':'OBNOXIOUS','БАНКИ/КАНИСТРЫ':'CANS',
                'ПРОБЕГ':'MILEAGE','ДИАПАЗОН/РЯД':'RANGE','ГИЕНА':'HYENA','ИЗМЕНЯТЬ':'TO CHEAT','НАМАТЫВАТЬ(КАТУШКУ)':'TO REEL',
                'СРАТЬ':'TO POO','КУРОРТ':'RESORT','ОТРЫВАТЬСЯ/ПРОВОДИТЬ ВРЕМЯ':'TO LIVE IT UP','ЭЛЕКТРОСТАНЦИИЯ/ЛОКОМОТИВ':'POWERHOUSE',
                'КУХНЯ(ЛОКАЛЬНАЯ)':'CUISINE','НОЧНОЙ КОШМАР':'NIGHTMARE','РЕЗУЛЬТАТИВНОСТЬ':'EFFICIENCY','НЫТЬ':'TO BITCH',
                'СТРОКА/РЯД':'ROW','СДЕРЖИВАТЬСЯ':'TO HELD BACK','НИКОГДА НЕ СДАВАЙСЯ!':'NEVER BACK DOWN!',
                'ЯГОДЫ':'BERRIES','КЛАДБИЩЕ':'CEMETERY','БОГАТСТВО/СОСТОЯНИЕ':'WEALTH','НЕЗАМЕНИМЫЙ':'INDISPENSABLE',
                'МОЗОЛЬ':'CALLUS','ОТПЕЧАТКИ ПАЛЬЦЕВ':'FINGERPRINTS','КОЛЬЦО':'RIM','СТРОИТЕЛЬ':'CONSTRUCTION WORKER',
                'ЖУЛЬНИЧЕСТВО':'HUSTLE','ДУБ':'OAK TREE','РАКЕТА':'MISSILE','ЕДИНОРОГ':'UNICORN',
                'МЕСТО В СОСТАВЕ':'ROSTER SPOT','БУНТ/МЯТЕЖ':'RIOT','ОТМЕНЕНО/ОТМЕНЕНЫ':'REVOKED','ПРОБА/ПОПЫТКА':'TRYOUT',
                'Я В ВОСТОРГЕ!':'I AM THRILLED!','АРЕНДОДАТЕЛЬ/ДОМОВЛАДЕЛЕЦ':'LANDLORD','ПРОВОКАЦИЯ':'ENTRAPMENT',
                'ЭКСКЛЮЗИВНЫЙ/ВЫСОКОКЛАССНЫЙ':'UPSCALE','БЛАГОТВОРИТЕЛЬНОСТЬ':'CHARITY','ОБЕСПЕЧЕННЫЙ':'WELL-OFF',
                'КЛЮЧИЦА':'COLLARBONE','ЭКИПИРОВКА':'GEAR','БУЛОЧКИ':'BUNS','СУДЬБА/УЧАСТЬ':'FATE','ОБРУЧАЛЬНОЕ КОЛЬЦО':'PROMISE RING',
                'НАРЯД/КОСТЮМ':'OUTFIT','МЕЛКИЕ РАСХОДЫ/НЕПРЕДВИДЕННЫЕ РАСХОДЫ':'INCIDENTALS','СОМНЕНИЯ':'QUALMS',
                'УБОГИЙ':'SHABBY','ПОЛАГАЮ/ПРЕДПОЛОГИЮ':'PRESUME','УКАЗ/ПОСТАНОВЛЕНИЕ':'DECREE','ПРОЩАЛЬНЫЙ(ПР.КОНЦЕРТ)':'FAREWELL',
                'ОБЛОМ':'BUMMER','ИСПОРЧЕННЫЙ/ЗАРАЖЕННЫЙ':'TAINTED','СДЕЛАЙ ПАУЗУ!':'PINCH IT OFF!','БРАКОНЬЕР':'POACHER',
                'ЩЕДРОСТЬ':'BOUNTY','МРАЧНЫЙ':'GLOOMY','ЛЕСОПИЛКА':'SAWMILL','ЛОБКОВЫЙ ВОЛОС':'PUBE','ПРИДУРКИ':'DORKS',
                'БАБНИК/ДОНЖУАН':'PHILANDERER','НЕВИННЫЙ/БЕЗВИННЫЙ':'INNOCENT','ЩЕЛЬ':'CHINK','ПОДКЛЮЧАТЬ':'TO PLUG',
                'ПОЗВОЛЯТЬ СЕБЕ':'TO AFFORD','КОРОЛЕВСКИЙ/ЦАРСКИЙ':'ROYAL','ПООБЩАТЬСЯ':'TO MINGLE','РАЗДОБЫТЬ':'TO RUSTLE UP',
                'ПРОКОЛОТЬ':'TO IMPALE','ВТОРЖЕНИЕ':'INVASION','ВЫСКОЧКА':'JUMPED-UP','НАСТАИВАТЬ':'TO INSIST',
                'КУЧЕРЯВЫЙ':'CURLY','ШАХТА':'SHAFT','КРОМЕШНАЯ ТЬМА':'PITCH BLACK','ШИНА/ПОКРЫШКА':'TYRE','РУЛЬ/КОЛЕСО':'WHEEL',
                'НЕУДОБСТВО/НЕПРИЯТНОСТЬ':'NUISANCE','МЕТКО':'APTLY',}

    vocabulary_update={value:key for key, value in vocabulary.items()}

    print('Слов в словаре:', len(vocabulary))
    pickle.dump(vocabulary_update, file)
    file.close()


main()