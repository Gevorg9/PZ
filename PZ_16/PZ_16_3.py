# для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранить информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате

import pickle
from PZ_16_1 import Cir


def save_def(cir, file):
    with open(f'{file}.bin', 'wb') as file:
        pickle.dump(cir, file)

def load_def(file):
    with open(f'{file}.bin', 'rb') as file:
        return pickle.load(file)

circle0 = Cir(5)
circle1 = Cir(10)
circle2 = Cir(20)

save_def(circle0, "circle0")
save_def(circle1, "circle1")
save_def(circle2, "circle2")
