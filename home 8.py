# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное,
# то выдаёт слово “чётное”, если нет - то “не чётное”.
t = lambda x: 'четное' if x % 2 == 0 else 'не четное'
print(t(4))
print(t(3))