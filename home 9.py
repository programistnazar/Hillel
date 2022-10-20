# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число,
# а значение - сколько раз оно встречается). Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in.
t = [2, 3, 4, 3, 2, 5]
d = {}


def analysis(t, d):
    for i in t:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for item in d:
        print("'%d' :%d" % (item, d[item]))


analysis(t, d)

