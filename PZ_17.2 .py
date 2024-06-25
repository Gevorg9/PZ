#Разработать программу с применением пакета tk
#Используя словарь посчитать количество уникальных слов в заданном
#предложении «Изучаем язык Питон». Вывести на экран каждую пару
#«ключ:значение».
import tkinter as tk


window = tk.Tk()
window.title("Количество уникальных слов")


word_counts = {}


def get_sentence():
    sentence = entry.get()
    return sentence


def count_words():
    sentence = get_sentence()
    words = sentence.split()
    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1


def display_results():
    count_words()
    for word, count in word_counts.items():
        result_listbox.insert(tk.END, f"{word}: {count}")


entry = tk.Entry(window, width=50)
entry.pack()


count_button = tk.Button(window, text="Подсчитать слова", command=display_results)
count_button.pack()


result_listbox = tk.Listbox(window)
result_listbox.pack()


window.mainloop()