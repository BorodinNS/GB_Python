### lambda

def f(x):
    x**2
g = f

print(f(1))
print(g(1))

def f(x):
    return x**2
g = f   #переменная, которая хранит ссылку на фунцкию

print(type(f))
print(type(g))
print(f(4))
print(g(4))

################################################################################################################################################

def calc1(x):
    return x+10

def calc2(x):
    return x*10

def math(op, x): #op - операция, х - значение.
    print(op(x))

math(calc1, 10)
math(calc2, 10)

################################################################################################################################################

def sum(x, y):
    return x+y

def mylt(x,y):
    return x*y

def calc(op, a, b):
    print(op(a,b))
    return op(a,b)

calc(mylt, 5, 5)

# >>> >>> >>> >>> >>>

sum01 = lambda x, y: x+y 
""" def sum(x, y):
    return x+y """

mylt01 = lambda x, y: x*y
""" def mylt(x,y):
    return x*y"""

def calc(op, a, b):
    print(op(a,b))
    #return op(a,b)    

calc(sum01, 4, 5)

# >>> >>> >>> >>> >>>

calc(lambda x, y: x+y, 4, 5)  #заменяет строку №47

################################################################################################################################################

#List Comprehension

list = []
for i in range (1, 21):
    if(i%2==0):
        list.append(i)
print(list)

# >>> >>> >>> >>> >>>

list01 = [i for i in range(21, 41) if i%2 == 0]
print(list01)

list01 = [(i, i) for i in range(21, 41) if i%2 == 0]  #добавление кортежей чисел
print(list01)

################################################################################################################################################
def f(x):
    return x**3

list02 = [f(i) for i in range(1, 21) if i%2 == 0]
print(list02)

def f(x):
    return x**3

list03 = [(i, f(i)) for i in range(1, 21) if i%2 == 0] #добавление кортежей
print(list03)












numbers = [1, 2, 3, 5, 8, 15, 23, 38]
def f(x):
    return x**3
numbers = [f(i) for i in numbers if i%2 == 0]
print(numbers)    