#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

""" num = abs(float(input('Введите вещественное число: ')))
sum = 0
for i in str(num):
    if i.isdigit():
        sum = sum + int(i)
print('Сумма цифр  равна: ', sum) """

#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

""" num = abs(int(input('Введите число N: ')))
i = 1
fibbo = 1
fibbo_list = list(range(1, num+1))
for i in range(1, num+1):
    fibbo *= i
    print(f'Произведение чисел от 1 до {i} = ', fibbo)
    fibbo_list[i-1] = fibbo
print(fibbo_list) """

#3. Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

""" import random

n_list = []
for i in range(0, (int(input('N: ')))):
    n_list.append(random.randint(-99, 100))
print(n_list,end=' => ')
for i in range(0, len(n_list)+1):
    if(n_list[i]<0):
        n_list.insert(i+1,0)
        i+=1
print(n_list) """

#4. Составьте алгоритм нахождения случайного числа без использования библиотеки random.

""" import datetime as t
import time


def prng(bbottom=-10,btop=10):
    if bbottom<0:
        btop+=abs(bbottom)
    seed=int(t.datetime.now().microsecond/(1000000/btop))
    return seed-abs(bbottom)

for _ in range(15): #для проверки
    time.sleep(0.3)
    print(prng(-50,50)) """