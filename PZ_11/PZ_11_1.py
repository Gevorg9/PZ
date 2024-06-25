'''
Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:

Исходные данные:
Количество элементов:
Отрицательные нечетные элементы:
Сумма отрицательных нечетных элементов:
Среднее арифметическое отрицательных нечетных элементов:

'''

import random
file_0 = open('file_0.txt','w',encoding='Utf-8')
file_1 = open('file_1.txt','w',encoding='Utf-8')
l1 = []


for i in range(random.randint(1,6)):
    x = random.randint(-5, 6)
    l1.append(x)
    file_0.write(str(x))
    file_0.write(' ')
file_1.write('Исходные данные: ')
file_1.write(str(l1))
file_1.write('\nКоличество элементов: ')
file_1.write(str(len(l1)))
file_1.write('\nОтрицательные нечетные элементы: ')
l_neg_odd = []
for i in l1:
    if i % 2 == 1 and i*-1>0:
        l_neg_odd.append(i)
file_1.write(str(l_neg_odd))
file_1.write('\nСумма отрицательных нечетных элементов: ')
file_1.write(str(sum(l_neg_odd)))
file_1.write('\nСреднее арифметическое отрицательных нечетных элементов: ')
try:
    file_1.write(str(sum(l_neg_odd)/len(l_neg_odd)))
except:
    file_1.write('0')