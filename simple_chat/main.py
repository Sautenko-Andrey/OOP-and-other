from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_async, run_js

import asyncio
import random
import json
from collections import OrderedDict

with open('/home/andrey/Python Projects/OOP-and-other/voc.json') as f:
    all_words = json.load(f)


def shuffle_dict(voc):
    keys = list(voc.keys())
    random.shuffle(keys)
    return OrderedDict([(k, voc[k]) for k in keys])

# res=shuffle_dict(all_words)
# print(res, type(res))


class Product:

    MIN_VALUE=0
    MAX_VALUE=1000

    @classmethod
    def __check_product_value(cls,value):
        if isinstance(value,float):
            return cls.MAX_VALUE>value>cls.MIN_VALUE
        raise ValueError('Value must be float!')

    @staticmethod
    def intro():
        print('we are product company....bla...bla...bla')

    def __new__(cls, *args, **kwargs):
        print('Creating new product....')
        return super().__new__(cls)

    def __init__(self,name:str,value:float):
        self.__check_product_value(value)
        self.name=name
        self.value=value

    def get_product_info(self):
        return self.name, self.value

    def set_product_info(self,name,value):
        self.name=name
        self.value=value

    def __getattribute__(self, item):
        if item=='salo':
            raise ValueError('Sorry, forbidden acces!')
        else:
            return object.__getattribute__(self,item)

    def __setattr__(self, key, value):
        if key=='salo':
            raise AttributeError('You can\'t set this product!')
        else:
            object.__setattr__(self,key,value)

    def __getattr__(self, item):
        print('There is no product you were asking for!')
        return False

    def __delattr__(self, item):
        print('Product deleted')
        object.__delattr__(self,item)

coca_cola=Product('Coca Cola',61.54)
print(coca_cola.get_product_info())
coca_cola.set_product_info('Кока Кола',65.00)
print(coca_cola.get_product_info())
salo=Product('salo',250.56)
print(salo.get_product_info())
salo.set_product_info('сало',277.0)
print(salo.get_product_info())





