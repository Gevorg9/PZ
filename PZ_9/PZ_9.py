#Используя словарь посчитать количество уникальных слов в заданном
#предложении «Изучаем язык Питон». Вывести на экран каждую пару
#«ключ:значение»
j = {}
sentence = "изучаем язык язык питон"
for word in sentence.split():
   if word not in j:
       j[word] = 1
   else:
       j[word] += 1

print(j)

for key, value in j.items():
   print(key + ":" + str(value))

