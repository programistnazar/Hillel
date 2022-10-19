# Сделать программу в виде функций в которой нужно будет угадывать число.
import random
number = random.randint(1, 10)


def my_num(secondcall=False):
    print("Загадано число от 1 до 10, отгадайте какое?")
    x = int(input())
    if x == number:
        print("Ты угадал мое число!")
        return
    if not secondcall:
        if x < number:
            print('нужно больше')
        else:
            print('нужно меньше')
        if number % 2 != 0:
            print('подсказка: число нечетное')
        else:
            print('подсказка: число четное')
        my_num(True)
    else:
        print("Не угадал! Я загадал число {0}".format(number))


my_num()