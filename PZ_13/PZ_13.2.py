#В матрице отрицательные элементы возвести в квадрат.

import random

# Генерация случайной матрицы произвольного размера
rows = 4
cols = 4
matrix = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

# Функция для возвышения отрицательных элементов в квадрат
def square_negatives(value):
    return value ** 2 if value < 0 else value

# Функция для обработки матрицы
def process_matrix(matrix):
    new_matrix = []
    for row in matrix:
        new_row = list(map(square_negatives, row))
        new_matrix.append(new_row)
    return new_matrix

# Обработка матрицы
new_matrix = process_matrix(matrix)

# Вывод результатов
print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nМатрица после возведения отрицательных элементов в квадрат:")
for row in new_matrix:
    print(row)