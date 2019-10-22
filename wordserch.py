import csv
from collections import Counter
import ctypes
csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))

filename = 'mts.csv'

mas = []
with open(filename, 'r', encoding='utf8', newline='') as file:  #открытие файла
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(row)):
            mas.append(row[i])


def word_func(elem):                                                    #функция разбиения на слова
    word = elem.split()
    q = 0
    mas1 = []
    while q < len(word):
        mas1.append(word[q])
        q += 1
    return(mas1)

oneword = []
for j in range(len(mas)):                                           #массив со всеми словами
    oneword.append(word_func(mas[j]))

oneword1 = []
for j in  range(len(oneword)):                                      #добавление слов в массив для подсчета кол-ва
    for i in range(len(oneword[j])):
        oneword1.append(oneword[j][i])

counter = Counter(oneword1)
print("Самое часто встречающееся слово:", counter.most_common(1))


def pair_func(elem):                                                    #функция разбиения на пары слов
    word = elem.split()
    g = 0
    mas2 = []
    while g + 1 < len(word):
        mas2.append(word[g] + ' ' + word[g + 1])
        g += 1
    return(mas2)

twoword = []
for j in range(len(mas)):                                          #массив со всеми парами слов
    twoword.append(pair_func(mas[j]))


twoword1 = []
for j in range(len(twoword)):                                     #добавление пар в массив для подсчета кол-ва
    for i in range(len(twoword[j])):
        twoword1.append(twoword[j][i])

counter1 = Counter(twoword1)
print("Самая часто встречающаяся пара слов:", counter1.most_common(1))


def three_func(elem):                                                  #функция разбиения на тройки слов
    word = elem.split()
    i = 0
    mas3 = []
    while i + 2 < len(word):
        mas3.append(word[i] + ' ' + word[i + 1] + ' ' + word[i + 2])
        i += 1
    return(mas3)

threeword = []
for j in range(len(mas)):                                          #массив со всеми тройками слов
    threeword.append(three_func(mas[j]))

threeword1 = []
for j in range(len(threeword)):                                   #добавление троек в массив для подсчета кол-ва
    for i in range(len(threeword[j])):
        threeword1.append(threeword[j][i])

counter2 = Counter(threeword1)
print("Самая часто встречающаяся тройка слов:", counter2.most_common(1))