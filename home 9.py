# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in.
t = [2, 3, 4, 3, 2, 5]
d = {}


def analysis(x, y):
    for i in x:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    for i in y:
        print("%d: %d" % (i, y[i]))


analysis(t, d)

