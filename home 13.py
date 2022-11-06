# Написать программу, которая состоит из вечного цикла ожидающего ввод числа
# или одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать
# введённые числа. Сама функция ничего не распечатывает, она возвращает строку,
# типа: "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное
# число: Erdf". Затем в цикле выводится это сообщение и цикл начинается заново
# ожидая следующего ввода. Функция на вход принимает строку из ввода из вечного
# цикла. Анализирует её исключительно методом .isdigit() и другими методами
# строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же
# распознаёт десятичные дроби как с точкой, так и с запятой.
# Функция возвращает строку в которой описывается какое число введено -
# отрицательное или положительно, целое или дробное и выводит его или же
# сообщает, что введено не корректное число.
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля
#
# Примеры:
# -6,7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -.777 → Вы ввели отрицательное дробное число: -0.777


def my_num(a):
    a = a.replace(',', '.')
    if a.replace('-', '', 1).isdigit():
        a = int(a)
        if int(a) > 0:
            return f'Вы ввели положительное целое число: {a}'
        elif int(a) == 0:
            return f'Вы ввели целое число: {a}'
        else:
            return f'Вы ввели отрицательное целое число: {a}'
    if a.replace('-', '', 1).replace('.', '', 1).isdigit():
        a = float(a)
        if float(a) > 0:
            return f'Вы ввели  дробное число: {a}'
        else:
            return f'Вы ввели отрицательное дробное число: {a}'
    else:
        return f'Вы ввели не корректное число: {a}'


def main():
    while True:
        x = input('Введите число или значения выхода из функции( "выход"/"exit"/"quit"/"e"/"q"): ')
        if x.lower() in ("выход", "exit", "quit", "e", "q"):
            break
        else:
            print(my_num(x))


main()
