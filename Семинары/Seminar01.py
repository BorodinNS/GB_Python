#1- Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
""" print('Введите первое число:')
num1 = int(input())
print('Введите второе число:')
num2 = int(input())
if num1 == (num2*num2) or num2 == (num1*num1):
    print('Одно из чисел является квадратом другого')
else:
    print('Ни одно из чисел не является квардатом другого') """

#2- Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
""" print('Введите 5 чисел через пробел:')
numbers = input().split()
maximum = int(numbers[0])
for i in numbers:
    i = int (i)
    if maximum < i:
        maximum = i
print(maximum) """

#3- Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
""" print('Введите число N:')
num_N = int(input())
num_n = num_N * -1
print(num_n)
while num_n < num_N:
    num_n = num_n+1
    print(num_n)
"""
#Решение через список
""" number = int(input('Введите число N:'))
opposite_number = -number
if number > opposite_number:
    new_range = list(range(opposite_number, number+1))
else:
    new_range = list(range(number, opposite_number+1))
print(new_range) """

#4-Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
print('Введите число:')
num_float = float(input())
num_int = int(num_float)
decimal = num_float - num_int
print(num_float)
print(abs(int(decimal*10)))
