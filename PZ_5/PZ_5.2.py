#Описать функцию PowerA234(параметры), вычисляющую вторую, третью и
#четвертую степень числа A и возвращающую эти степени соответственно в
#переменные B, C и D. С помощью этой функции найти вторую, третью и четвертую
#степень пяти данных чисел.


def PowerA234(A):
   B = A ** 2
   C = A ** 3
   D = A ** 4
   return B, C, D


try:
   numbers = [int(input("Введите число: ")) for _ in range(5)]
   for number in numbers:
       try:
           B, C, D = PowerA234(number)
           print(f"Число: {number}, Вторая степень: {B}, Третья степень: {C}, Четвертая степень: {D}")
       except TypeError:
           print("Некорректный тип данных. Пожалуйста, введите целое число.")
except ValueError:
   print("Ошибка ввода. Пожалуйста, введите целое число.")






