# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def simple_multiplier():
    """Список простых множителей числа N"""
    n = int(input('Введите число N: '))
    nums = list()
    multiplier = 2
    while n >= multiplier:
        while n % multiplier == 0:
            n /= multiplier
            nums.append(multiplier)
        multiplier += 1
    nums = list(set(nums))
    nums.sort()
    print('Список простых множителей числа N:', nums)


# simple_multiplier()

# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#Не использовать множества.
def not_repeating_elements():
    """Ввод списка и вывод неповторяющихся элементов в нём"""
    numbers = input('Введите список элементов через пробел: ')
    numbers = list(map(int, numbers.split()))
    unique = []
    for i in numbers:
        if i in unique:
            continue
        else:
            unique.append(i)
    print('Введённая последовательность чисел:\t', numbers)
    print('Список элементов без повторений:\t', unique)
not_repeating_elements()

# 3. В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».
from typing import List

def change_list(file: List[str], for_change: str) -> str:
    """ Принимает список, возвращает список с большими буквами """
    new_list = ''
    for i in file:
        if i.count(for_change):
            i = i.upper()
        string = i + '\n'
        new_list += string
    return new_list

new_list = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Homework\HW04.txt', 'r', encoding='utf-8')
lines_read = new_list.read().split('\n')
new_list.close()

result_list = change_list(lines_read, for_change = '5')

new_list = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Homework\HW04.txt', 'w', encoding='utf-8')
new_list.write(result_list)
new_list.close()

#4. Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо,
# "юяяю" - сдвиг на 2 влево.
#Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, 
# считывает текст и дешифровывает его.
def get_encript_text(alphabet: str, text: str, key: int) -> str:
    """ Принимает строку, возвращает зашифрованную строку 
    Args:   alphabet - алфавит
            text - строка подлежащая шифрованию
            key - смещение
    Return: str - зашифрованная строка"""
    encript_text = ''
    alphabet_long = len(alphabet)
    for simbol in text:
        i = 0
        #index = alphabet.find(simbol)
        for s in alphabet:
            if simbol == s:
                index = i + key
            i += 1
        if index > alphabet_long:
            index -= alphabet_long  
        encript_text += alphabet[index]
    return encript_text

def get_decript_text(alphabet: str, text: str, key: int) -> str:
    """ Принимает зашифрованную строку, возвращает расшифрованную строку 
    Args:   alphabet - алфавит
            text - строка подлежащая шифрованию
            key - смещение
    Return: str - зашифрованная строка"""
    decript_text = ''
    alphabet_long = len(alphabet)
    for simbol in text:
        i = 0
        #index = alphabet.find(simbol)
        for s in alphabet:
            if simbol == s:
                index = i - key
            i += 1
        if index < 0:
            index = alphabet_long + index
        if index >= alphabet_long:
            index = index - alphabet_long
        decript_text += alphabet[index]
    return decript_text


alphabet = 'AБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдийклмнопрстуфхцчшщьыъэюя'
text_for_change = 'Шла Маша по шоссе и сосала сушку'
key = 1

encript_text = get_encript_text(alphabet, text_for_change, key)
file_encript = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Homework\encript.txt', 'w', encoding='utf-8')
file_encript.write(encript_text)
file_encript.close()


file_encript = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Homework\encript.txt', 'r', encoding='utf-8')
enc_text = file_encript.read()
file_encript.close()

decript_text = get_decript_text((alphabet, enc_text, key))
file_decript = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Homework\decript.txt', 'w', encoding='utf-8')
file_decript.write(decript_text)
file_decript.close()
