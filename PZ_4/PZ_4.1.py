#Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа,
#расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.
def print_numbers(A, B):
    if A > B:
        print("Ошибка: A должно быть меньше B")
        return

    count = 0
    while A <= B:
        print(A)
        A += 1
        count += 1

    print("Количество чисел:", count)


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print_numbers(A, B)