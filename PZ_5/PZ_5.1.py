#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится ноль?


def subtract_digits(num):
   count = 0
   while num != 0:
       digits_sum = sum(int(digit) for digit in str(num))
       num -= digits_sum
       count += 1
   return count




try:
   num = int(input("Введите число: "))
   result = subtract_digits(num)
   print("Число вычтений:", result)
except ValueError:
   print("Ошибка ввода. Пожалуйста, введите целое число.")




