# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_load.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.
import time


class Auto:
    def __init__(self, brand, age, mark, weight=1000, color='red'):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.weight = weight
        self.color = color

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1




class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, weight=1000, color='red'):
        super().__init__(brand, age, mark, weight, color)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
        print(f'max_load is {self.max_load}')


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, weight=1000, color='red'):
        super().__init__(brand, age, mark, weight, color)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')


t1 = Truck('Volvo', 20, 'r2', 500)
t2 = Truck('Bmw', 10, '3', 300)
t1.move()
t2.move()
print(t1.color)
print(t2.color)
print(t1.brand)
print(t2.brand)
print(t1.age)
print(t2.age)
print(t1.weight)
print(t2.weight)
print(t1.mark)
print(t2.mark)
print(t1.max_load)
print(t2.max_load)
t1.birthday()
t2.birthday()
t1.load()
t2.load()
t1.stop()
t2.stop()

c1 = Car('fiat', 10, 'classic', 200)
c2 = Car('reno', 20, 'megan', 220)
c1.move()
c2.move()
print(c1.color)
print(c2.color)
print(c1.brand)
print(c2.brand)
print(c1.age)
print(c2.age)
print(c1.weight)
print(c2.weight)
print(c1.mark)
print(c2.mark)
print(c1.max_speed)
print(c2.max_speed)
c1.birthday()
c2.birthday()
c1.stop()
c2.stop()