print("Hello World!")
#Типы данных и переменная
#int, float, boolean, str, list, None

a = 123 #int
b = 1.23 #float
print(a)
print(b)

value = None #Нельзя объявлять переменную, без значения! Используем "None"
value = 12345
print(value)

s = "HelloWorld" #string  #/n - перенос на новую строку
print(s)

#Функция "type" позволяет узнать тип переменной
#print(type(value))
#print(type(s))

print(a, '-', b, '-', value, '-', s)
print('{} - {} - {} - {}'.format(a, b, value, s))
print(f'{a} - {b} - {value} - {s}')

f = True #тип boolean
print(f)

list = [1, 2, 3, 'hello', '1', '2', '3'] #аналог массива
print(list)

#Ввод и вывод данных
print('Введите a:')
a = input() #Значение воспринимается как строка
print('Введите b:')
b = input()
print(a, "+", b, "=", a+b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

#Чтобы производить вычисления, необходимо добавить тип данных
print('Введите a:')
a = int(input())
print('Введите b:')
b = int(input())
print(a, "+", b, "=", a+b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

#Арифметические операции: 
# +, -, *, /, %, // деление в целых числах, ** возведение в степень
a = 1.3
b = 3
c = round(a*b, 3) #round - математическое округление. 3 - кол-во цифр после запятой
print(c)

a = 3
a = a + 5  #== a+=5
print(a)
#iter += 3 # iter = iter + 3
#iter -= 4 # iter = iter - 4
#iter *= 5 # iter = iter * 5
#iter /= 5 # iter = iter / 5
#iter //= 5 # iter = iter // 5
#iter %= 5 # iter = iter % 5
#iter **= 5 # iter = iter ** 5

#Логические операции:
#>, >=, <, <=, ==, !=
#not, and, or - не путать с &, |, ^
#is, is not, in, not in

a = 1 < 4
print(a)

a = 1 < 4 and 2 < 5
print(a)

a = [1, 2]
b = [1, 2]
print(a == b)

a = 1 < 3 < 5 < 10
print(a)

f = 1 > 2 or 4 < 6
print(f)

func = 1
T = 4
x = 2
print(func < T > x)

f = [1, 2, 3, 4]
print(f)
print(not 2 in f)
print(2 in f)

#Управляющие конструкции:
#if, if-esle, elif
#if условие:
    #операции
#else:
    #операции
a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждал Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ!')
else:
    print('Привет, ', username)

#while
#while условие
    #операции
#Переворот числа
original = 58
inverted = 0
while original != 0:
    inverted = inverted * 10 +(original % 10)
    original //= 10
print(inverted)

#Довавляем else
original = 205
inverted = 0
while original != 0:
    inverted = inverted * 10 +(original % 10)
    original //= 10
else:
    print('Пожалуй ')
    print('Хватит')
print(inverted)

#for
#for i (счетчик) in объект (список)
    #операции
list =[1,2,3,10,5]
for i in list:
    print(i)

r = range(10)
for i in r:
    print(i)

for i in range(1,10,2): #(от 1 до 10, счетчик 2)
    print(i)

#Немного о строках
text = 'съешь еще этих мягких французских булок'
print(len(text)) #кол-во символов в строке
print('еще' in text) #проверка наличия #True
print(text.isdigit()) #являются ли все символы числами #False
print(text.islower()) #являются ли все символы маленькими #True
print(text.replace('еще', 'ЕЩЕ')) #замена 


text = 'съешь еще этих мягких французских булок'
print(text[0]) #c
print(text[1]) #ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#Списки
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]

numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e) # red green blue
for e in colors:
    print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент

#Функции
#Это фрагмент программы, используемый многократно
#def function_name(x):
# body line 1
# . . .
# body line n
 # optional return
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
