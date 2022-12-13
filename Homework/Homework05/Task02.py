#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candies = 117
limit = 28
player = randint(1, 2)
step = 1
print(f'Всего конфет: \033[1m\033[31m{candies}\033[0m, максимально можно взять {limit}')
while candies != 0:
    if player == 1:
        who = 'человек'
    else:
        who = 'компьютер'
    print(f'\033[1;30mХод {step}\033[0m. Количество конфет: \033[1m\033[36m{candies}\033[0m. Ход игрока: {who}')
    if player == 1:  # ход человека
        amount = limit + 1
        while amount > limit or amount < 1 or amount > candies:
            amount = int(input('Сколько берете конфет? '))
            if amount > limit or amount < 1:
                print(f'Вы должны выбрать от 1 до {limit}, введите повторно')
        player = 2
    else:  # ход компьютера
        if candies % (limit + 1) == 0:
            amount = randint(1, limit)
        elif candies > limit:
            amount = candies % (limit + 1)
        else:
            amount = candies
        print(f'Компьютер взял конфет: {amount}')
        player = 1
    step += 1
    candies -= amount
if player == 2:
    print('Вы выиграли!')
else:
    print('Выиграл компьютер')
