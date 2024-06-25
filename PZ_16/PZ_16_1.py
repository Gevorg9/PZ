# Создать класс "круг", который имеет атрибут радиуса и методы
# для вычисления площади, длинны окружности и диаметра
class Cir:
    def __init__(self,r):
        self.r = r

    def dia(self):
        return self.r*2
    def len(self):
        return self.r*3.14*2
    def pl(self):
        return self.r**2*3.14
a = Cir(100)
print(a.dia())
