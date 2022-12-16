# Составить список четных значений и их квадрата из файла.
path = 'D:\Обучение\GeekBrains\Вторая четверть\Python\Лекции\Lecture03\Lecture03_file.txt'
f = open(path, 'r')
data = f.read() + ' ' #искуственно считываем строки и добавляем пробел
f.close

numbers = [] #создание пустого списка для дальнейшего заполнения

while data != '':                               #пока строка не пустая
    space_pos = data.index(' ')                 #нахождение позиции первого пробела
    numbers.append(int(data[:space_pos]))       #взять всё, что до пробела, превращение в число и добавление в список
    data = data[space_pos+1:]                   #обновление строки с учетом уже обработанного

out = []
for e in numbers:
    if not e%2:
        out.append((e, e**2))
print(out)


# >>> >>> >>> >>> >>> улучшение решения

def select(f, col): #f - функция, col - данные
    """ Принимает функцию и данные для обработки """
    return [f(x) for x in col]

def where(f, col):
    """ Условие фильтрации объектов """
    return [x for x in col if f(x)]

data1 = '1 2 3 5 8 15 23 38 40'.split()

res = select(int, data1)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print(res)