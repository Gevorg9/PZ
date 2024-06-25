#Сформировать и вывести целочисленный список размера 10,
#содержащий 10 первых положительных нечетных чисел: 1,3,5, ... .


numbers = []
count = 1

while len(numbers) < 10:
  if count % 2 != 0:
      numbers.append(count)
  count += 1


print(numbers)
