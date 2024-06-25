# из текстового файла (writer.txt) выбрать фамилии писателей, подсчитать колличество
# фамилий. Создать новый файл , в котором выполнить замену слова "роман" на слово
# "произведение"
import re

f = open('writer.txt', 'r', encoding='UTF-8')

familia = re.findall(r'([А-ЯЁA-Z][\w+-]+) \w[,.]\w',f.read())
print(familia)
f2 = open('writer_redux.txt','w',encoding='Utf-8').write(open('writer.txt','r',encoding='Utf-8').read().replace('роман','произведение'))
f.close()
print('кол-во элементов:',len(familia))
