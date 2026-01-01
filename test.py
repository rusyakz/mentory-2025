from functools import wraps


def decor(func):
    #@wraps(func)
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return result
    return wrapper

#@decor
def test(name):
    '''Тестовая функция'''
    return "Hello " + name


test1 = decor(test)

test1("test")

print(test1.__name__)
print(test1.__doc__)
print(dir(test1))



class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


dog1 = Dog("Miki")
print(dog1.name)