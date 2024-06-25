#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых
# и последних строках и столбцах матрицы Matr2 произвольного размера.
import random

# Генерация размера матрицы Matr2
rows = 5
cols = 5
Matr2 = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Эта Функция для проверки является ли элемент "экстерьорным"
def is_exterior_element(row, col, rows, cols):
    return row not in (0, rows - 1) and col not in (0, cols - 1)

# Функция для переноса элементов в новую матрицу
def transfer_exterior_elements(Matr2):
    Matr1 = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if is_exterior_element(i, j, rows, cols):
                row.append(Matr2[i][j])
        if row:
            Matr1.append(row)
    return Matr1

# Переносим элементы в новую матрицу Matr1
Matr1 = transfer_exterior_elements(Matr2)

# Вывод результатов
print("Исходная матрица Matr2:")
for row in Matr2:
    print(row)

print("\nНовая матрица Matr1 (экстерьорные элементы):")
for row in Matr1:
    print(row)