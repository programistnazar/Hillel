# Написать декоратор к 2-м любым функциям, который бы считал и
# выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()
from datetime import datetime


def my_decorator(a_function):
    def timer():
        time = datetime.now()
        a_function()
        time_2 = datetime.now() - time
        print('Время начала выполнения функции: ', time)
        print('Продолжительность выполнения функции: ', time_2)

    return timer


@my_decorator
def wars():
    print('Hello, world')


@my_decorator
def cor():
    print(int(1+2+4))


wars()
cor()


