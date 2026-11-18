# вариант 14
# 1  Область видимости
x = 24

def show():
    x = 14
    print(x)

show()
print(x)
# вывод: 
# 14
# 24
# внутри функции show используется локальная переменная x = 14.
# снаружи используется глобальная переменная x = 24.

# 2  Args
def total(*args):
    return sum(args)

print(total(14, 15, 16))

# 3  Kwargs
def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Денис", age=20))

# 4  Функция как параметр
def increase(x):
    return x + 4

def apply(func, value):
    return func(value)

print(apply(increase, 3))

# 5  Рекурсия
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(3)
