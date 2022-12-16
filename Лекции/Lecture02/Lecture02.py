# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных

# a
colors = ['red', 'green', 'blue']
data = open('D:\Обучение\GeekBrains\Вторая четверть\Python\Лекции\Lecture02\Lecrure02.txt', 'a')
data.writelines(colors) #разделителей не будет
data.close
exit

#Тоже самое, но короче
with open('D:\Обучение\GeekBrains\Вторая четверть\Python\Лекции\Lecture02\Lecrure02.txt', 'a') as data:
    data.write('line1 \n')
    data.write('line2 \n')

# r
path = 'D:\Обучение\GeekBrains\Вторая четверть\Python\Лекции\Lecture02\Lecrure02.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close
exit

import Hello as h #приравнивает файл из первой лекции к h
print(h(1))