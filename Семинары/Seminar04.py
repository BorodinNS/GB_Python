# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
""" numbers = list(map(int, input('Введите числa через пробел: ').split( )))
print(max(numbers), min(numbers)) """

# 2. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.
# НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.
num1, num2 = map(int, input().split())

def search_nod(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def search_nok(num1, num2):
    return num1 * num2 / search_nod(num1, num2)

print(search_nok(num1, num2))

# 3. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Число N вводится пользователем. Позиции хранятся в файле ПозицииN.txt в одной строке одно число
# Изначально в файле до ввода N ничего нет.
# Позиции в файл вам нужно программно положить в зависимости от выбранного N: если пользователь введет двойку,
# то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.
""" from random import randint
def write_to_file(n):
    with open ('ПозицииN.txt', 'w') as file:
        for i in range(n):
            file.write(f'{randint(-n, n)}\n')

write_to_file(5) """
