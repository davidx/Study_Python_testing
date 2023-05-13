# myFile = open('.idea/namefile.txt', 'w')
# myFile.write('ttt')
# print('xxxx', file = myFile)
#


'''alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число, на которое нужно сдвинуть текст: '))

summary = ''


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open("filename2.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open("output.txt", 'w', encoding="utf8") as myFile:
    myFile.write(summary)'''


'''Herzeleid'''
import os


# myFile_Herz_L = open(r'D:\Документы\Herzeleid.txt', 'r+')
# myFile_Herz_L.write('Rammstein, Album "Herzeleid"')
# myFile_Herz_L.close()
# myFile_Herz_L = open(r'D:\Документы\Herzeleid.txt', 'r')
# print(myFile_Herz_L.readline())

# hh = os.path.join('..','..','new-p','Herzeleid — копия.txt')
# print(hh)
# mFile = open(hh)
# print(mFile.readline())

'''
программу, которая получает от пользователя имя файла,
открывает этот файл в текущем каталоге, читает его и выводит два слова:
наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.

В файле ожидается смешанный текст на двух языках — русском и английском.
'''

'''
'''

'''class User:
    def __init__(self, name, birth_date, home_state, gender):
        self.name = name
        self.birth = birth_date
        self.home_state = home_state
        self.sex = gender'''

# создан класс Юзер и к нему добавлен через конструктор класса набор аргументов
# наполнение аргументов сущностямя/объектами:

'''manfred = User(name = 'Mann von Groess',
               birth_date = '10.30.1977',
               home_state = 'Russia', gender = 'Male')

class Product:
    def __init__(self, name, category, stock):
        self.name = name
        self.cat = category
        self.stock = stock
    def is_in_stock(self):
        return True if self.stock > 0 else False

eggs = Product('eggs', 'food/meel', 10)

print(eggs.is_in_stock())'''

'''
events = [
    {
     "timestamp": 1554583508000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1555296337000,
     "type": "itemViewEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
    {
     "timestamp": 1549461608000,
     "type": "itemBuyEvent",
     "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
    },
]
class Event:
    def __init__(self, timestamp=0, event_type='', session_id=''):
        self.timestamp = timestamp
        self.type = event_type
        self.session_id = session_id

    def init_from_dict(self, event_dict): # even_dict - выполняет роль временной переменной, как в ф-иях
        self.timestamp = event_dict.get('timestamp')
        self.type = event_dict.get('type')
        self.session_id = event_dict.get('session_id')

# for event in events:
#     event_object = Event()
# event_object.init_from_dict(event)
print(event_object.timestamp,'\n',
          event_object.type)'''


# class Products:
#     def __init__(self, goods_id=0, name='',
#                  cost=0, stock=0, min_stock=0,which_animal='', weight_for_sell=0,
#                  date_of_prod=0):
#         self.id = goods_id
#         self.name_for_good = name
#         self.cost = cost
#         self.stock = stock
#         self.min_stock = min_stock
#         self.which_an = which_animal
#         self.weight = weight_for_sell
#         self.start_date = date_of_prod
#
#     def is_min_stock(self):
#         # return self.stock if self.stock > self.min_stock else False
#         return f'Наличие товара на минимуме - {self.stock}kg' if (self.stock <= (self.min_stock +1))\
#             else 'Товара достаточно'
#
#
# class Meat(Products):
#     is_in_food=True
#
# rabbit = Meat(goods_id=12324, cost=12.45, stock=6, which_animal='rabbit', min_stock=5)
#
# print(rabbit.stock, rabbit.cost)
# print(rabbit.is_min_stock())

# print(isinstance(rabbit, Meat))




