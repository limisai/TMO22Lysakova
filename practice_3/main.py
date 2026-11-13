g = (x * 5 for x in [1, 2, 3])
print(list(g))

def announce(func):
    def wrapper():
        result = func()
        print("Приветствуем")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()