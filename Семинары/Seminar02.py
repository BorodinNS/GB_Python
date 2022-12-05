#1 Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#Пример: для N = 5: 1, -3, 9, -27, 81
""" num = int(input('Введите число N: '))
res = 1
for i in range (num):                                #Если не указывать первое значение range(0, num+1) по дефолту будет с нуля
    print(res, end= ' ')
    res *= -3 """

#Более компактное решение:
""" for i in range(int(input())):
    print((-3)**i, end = ' ') """

#Словари
""" dct = {'кошка': 'cat', 'апельсин': 'orange'}
dct['молоко'] = 'milk'
print(dct.keys()) """

#
""" n = int(input())
dct = {}
for i in range (1, n+1):
    dct[i] = 3*i + 1
print(dct) """
#тоже самое, что и выше
""" dct = {i: 3*i + 1 for i in range(1, int(input())+1)}
print(dct) """

#Пользователь задаёт две строки, а программа проверяет количество вхождений
""" str1, str2 = input('Введите первую строку: ').lower(), input('Введите вторую строку: ').lower()
count = 0
# print(str1.count(str2)) #использование встроенной функции. Ищет вхождения стр2 в стр1
str1 = str1.split()
for i in str1:
    if i == str2:
        count+=1
print(count)

print(str1.count(str2)) #использование встроенной функции. Ищет вхождения стр2 в стр1 """