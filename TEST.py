
import pickle
from random import choice
def main():
    """
    Программа будет извлекать данные из файла словаря и предлагать для тестирования
    :return: None
    """
    #прочтем данные из файла:
    file = open('/home/andrey/Studying/vocabulary/my_vocabulary.dat', 'rb')
    #file=open('/home/andrey/Studying/vocabulary/my_vocabulary2.dat', 'rb')   #тест будет с русского на английский
    #file = open('/home/andrey/Studying/my_vocabulary3.dat', 'rb')   #тест будет с английского на русский
    end_of_file = False
    while not end_of_file:
        try:
            vocabulary = pickle.load(file)
        except EOFError:
            end_of_file = True
    file.close()
    test(vocabulary)

def test(some_vocabulary):
    right_answers=0
    kol_vopros=0
    try:
        for count in range(len(some_vocabulary)):
            key,value=some_vocabulary.popitem()
            print(key)
            user_answer=input('Напиши перевод слова: ').upper()
            kol_vopros+=1
            if user_answer==value:
                print('Правильно,молодец,Андрей:)')
                right_answers+=1
            else:
                print('ОШИБКА!!! Правильный ответ:',value)
    except ValueError as err:
        print(err)
    except KeyError as err2:
        print(err2)
    finally:
        print('Тест закончен! Андрей,ты хорошо поработал:)')
        print('Правильных ответов:',format((right_answers/kol_vopros)*100,'.2f'),'%')
main()