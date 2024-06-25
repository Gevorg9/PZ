'''Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку между первой и второй.'''
f = open('text18-1.txt','r',encoding='utf-8')
print(f.read())
f.seek(0)
uper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s = 0
for i in f:
    for j in i:
        if j in uper:

            s += 1
print('Колличество букв в верхнем регистре: ',s)
f.close()
lines = open('text18-1.txt','r',encoding='utf-8').read().strip().split('\n')
last_line = lines.pop()
lines.insert(1, last_line)
new_text = '\n'.join(lines)
with open("file.txt", "w", encoding='utf-8') as new_file:
    new_file.write(new_text)
