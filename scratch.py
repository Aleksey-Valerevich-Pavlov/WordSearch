import csv
import sys
from collections import Counter
csv.field_size_limit(sys.maxsize)

filename = 'mts.csv'

mas = []
mas1 = []

with open (filename, 'r', encoding='utf8', newline='') as file:  #открытие файла
    reader = csv.reader(file)
    for row in reader:
        i = 0
        while i<len(row):                                        #создание массива из НЕ одиночных слов
            if row[i].count(' ') > 0:
                mas.append(row[i])
            if row[i].count(' ') == 0:
                mas1.append(row[i])
            i += 1


def para(elem):                                                   #функция разбиения на пары слов
    word = elem.split()
    i = 0
    mas1 = []
    while i + 1 < len(word):
        mas1.append(word[i] + ' ' + word[i + 1])
        i += 1
    return (mas1)

def troika(elem):                                                 #функция разбиения на тройки слов
    word = elem.split()
    i = 0
    mas2 = []
    while i + 2 < len(word):
        mas2.append(word[i] + ' ' + word[i + 1] + ' ' + word[i + 2])
        i += 1
    return (mas2)

twowords = []
for j in range(len(mas)):                                          #массив со всеми парами слов
    twowords.append(para(mas[j]))

twowords1 = []
for j in  range(len(twowords)):                                    #добавление пар в массив для подсчета кол-ва
    for i in range(len(twowords[j])):
        twowords1.append(twowords[j][i])

threewords = []
for j in range(len(mas)):                                          #массив со всеми тройками слов
    threewords.append(troika(mas[j]))

threewords1 = []
for j in  range(len(threewords)):                                  #добавление троек в массив для подсчета кол-ва
    for i in range(len(threewords[j])):
        threewords1.append(threewords[j][i])

                                                                   #нахождение самых часто встречающихся слов, пар и троек
counter = Counter(mas1)
print("Самое часто встречающееся слово:", counter.most_common(1))

counter1 = Counter(twowords1)
print("Самая часто встречающаяся пара слов:",counter1.most_common(1))

counter2 = Counter(threewords1)
print("Самая часто встречающаяся тройка слов:",counter2.most_common(1))



