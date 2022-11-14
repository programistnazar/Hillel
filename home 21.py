# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

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


auto_1 = Auto('toyota', 10, 'corolla', 1500, 'green')
print(auto_1.age)
print(auto_1.brand)
print(auto_1.color)
print(auto_1.mark)
print(auto_1.weight)

auto_1.move()
auto_1.stop()
auto_1.birthday()

print(auto_1.age)

