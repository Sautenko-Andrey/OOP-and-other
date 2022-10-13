import random

import numpy as np


def activate(x):
    return 0 if x < 0.5 else 1


def girlsmind(house, rock, attractive):
    x = np.array([house, rock, attractive])  # вектор входного сигнала

    neyron11 = [0.3, 0.3, 0]  # веса для первого нейрона скрытого слоя
    neyron12 = [0.4, -0.5, 1]  # веса для торого нейрона скрытого слоя

    weight = np.array([neyron11, neyron12])  # объединение двух весов в матрицу

    vector_out = np.array([-1, 1])  # вектор связи для выходного нейрона

    sum_hidden = np.dot(weight, x)  # матричное умножение для получения суммы на каждом нейроне
    print(f'Значения сумм на нейронах скрытого слоя {sum_hidden}')

    out_hidden = np.array([activate(x) for x in sum_hidden])
    print(f'Значения на выходах нейронов скрытого слоя {out_hidden}')

    sum_end = np.dot(vector_out, out_hidden)

    y = activate(sum_end)

    print(f'Выходное значение нейронной сети: {y}')

    return y


# house=1
# rock=0
# attractive=1
#
# res=girlsmind(house,rock,attractive)
# if res==1:
#     print('I like you')
# else:
#     print('Goodbye!')

def man_activation(vector_entance):
    if vector_entance < 0.5:
        return 0
    else:
        return 1


def man_world(boobs, temper, kids):
    '''Нейросеть,имитирующая мозговую деятельность мужика
    при выборе женщины. Договоримся, что для каждого параметра на входе
    мы будем давать 1 за "да" и 0 за "нет".
    Сделаем 2 умозаключения, сформировав для них 2 нейрона:
    1) Если у нее есть дети, то сразу отвергаем ее.
    2) Если у нее есть сиськи и конченный характер, то все равно можно встретиться.
    Результирующая симпатия теперь будет формироваться если первое обобщение отсутствует,
     а второе присутствует'''

    # в саом начале формируем вектор входного сигнала на основе наших параметров
    entrance_vector = np.array([boobs, temper, kids])

    # Мы договорились, что 1 — это «да», а 0 — это «нет» при входе для каждого из параметров

    # далее прописываем веса для первого нейрона скрытого слоя для сисек и характера
    weight_11_neyron = [0.3, 0.3, 0]

    # формируем веса для второго нейрона для детей
    weight_12_neyron = [0.5, 0.4, -1]

    # объеденяем эти все веса в матрицу
    mututal_weight_matrix = np.array([weight_11_neyron, weight_12_neyron])

    # далее формируем вектор связи для выходного нейрона
    exit_weight = np.array([1, -1])

    # далее вычисляем сумму для всех скрытых нейронов
    sum_hidden_neyrons = np.dot(mututal_weight_matrix, entrance_vector)
    print(f'Сумма на каждом скрытом нейроне составляет {sum_hidden_neyrons}')

    # затем пропускаем каждую сумму через функцию активации и получаем вектора
    out_vector = np.array(man_activation(entrance_vector) for entrance_vector in sum_hidden_neyrons)
    print(f'Значения векторв на выходе {out_vector}')

    # вычисляем суммы на выходном нейроне
    sum_end = np.dot(exit_weight, out_vector)

    # пропускаем эту сумму через ф-ию активации
    result = man_activation(sum_end)
    print(f'Результат: {result}')

    return result


import matplotlib.pyplot as plt

N = 5

x1 = np.random.random(N)
x2 = x1 + [np.random.randint(10) / 10 for i in range(N)]
C1 = [x1, x2]

x1 = np.random.random(N)
x2 = x1 - [np.random.randint(10) / 10 for i in range(N)] - 0.1
C2 = [x1, x2]

f = [0,1]

