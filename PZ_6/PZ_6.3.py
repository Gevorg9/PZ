#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, не включая
#эти элементы.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 2
L = 5

reversed_list = numbers[:K] + numbers[K+1:L][::-1] + numbers[L+1:]


print(reversed_list)