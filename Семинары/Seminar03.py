from typing import Optional


def give_int(input_string: str,
             min_num: Optional[int] = None,
             max_num: Optional[int] = None) -> int:
    """ Выпытвает у пользователя число
    Args: input_string - предложение ввода
    Returns: int - число """
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите число больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите число меньше {max_num}')
                continue
            return (num)
        except ValueError:
            print('Вы ввели не число.')


#number = give_int('Введите число: ', min_num=5, max_num=20)


# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3
""" def find_element(new_list, find_in_list):
    count = 0
    switch = True
    for i in new_list:
        if i.find(find_in_list)!= -1:
            print(f'{find_in_list} содержится в элементе с индексом {count}')
            switch = False
        count+=1
    if switch:
        print('Элементов не найдено')
new_list = ['gfh5', 'gfh2', '67', 'jy32', '3put']
find_in_list = '32'
find_element(new_list, find_in_list) """

#2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#Пример: список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#список: [], ищем: "123", ответ: -1
""" new_list = ["123", "234", 123, "567"]
find_in_list = "123"
def find_func(new_list, find_in_list):
    count = 0
    n = -1
    for i in range(0, len(new_list)):
        a = new_list[i] == find_in_list
        if a:
            count+=1
        if count == 2:
            return i
    return n 
print(find_func(new_list, find_in_list)) """

#3. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
""" n = int(input())
dct = {}
for i in range (1, n+1):
    dct[i] = 3*i + 1
print(dct) """
