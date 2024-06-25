# Создайте класс "Фигура", который содержит метод расчета площади фигуры.
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
class Figure:
    def __init__(self):
        pass
    def pl(self):
        return 'площадь расчитывается только для конкретных фигур'

class Square(Figure):
    def __init__(self,a):
        super().__init__()
        self.a = a
    def pl(self):
        return self.a **2


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
    def pl(self):
        return self.a * self.b

# Пример использования:
sq = Square(5)
re = Rectangle(4, 6)

print(f"Площадь квадрата: {sq.pl()}")
print(f"Площадь прямоугольника: {re.pl()}")
