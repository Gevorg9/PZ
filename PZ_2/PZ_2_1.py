# Вариант № 25. С начало суток прошло N секунд (N - целое). Найти количество полных часов, прошедших с начало суток.

try:
    n = int(input("Введите количество секунд:")) #Вводим количество секунд с помощью функции input
    # и преобразуем его в целое число с помощью функции int
    if n < 0:
        raise ValueError #генерируем исключение, если введено отрицательное число
    hours = n//3600 #находим количество полных часов
    print("Количество полных часов:", hours) # Выводим количествополных часов
except ValueError:
    print("Введено некорректное значение. Введите положительное целое число.") # если возникло исключение ValueError,
    # выводим сообщение об ошибке












