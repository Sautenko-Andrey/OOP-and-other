from random import choice,randint

vocabulary={'first':'perviy','second':'vtoroy','third':'tretiy'}
# my_list=list(vocabulary.items())
# print(my_list)
# print('Слуйчано выбранное')
# print(choice(my_list))
for i in range(len(vocabulary)):
    res=list(vocabulary.items())
    print(choice(res[0]))