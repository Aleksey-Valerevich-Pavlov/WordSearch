import csv
import sys
from collections import Counter
csv.field_size_limit(sys.maxsize)

filename = 'mts.csv'
mas = []
mas1 = []
mas2 = []

with open (filename, 'r', encoding='utf8', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        i=0
        while i<len(row):
            if row[i].count(' ') == 0:
                mas.append(row[i])
            if row[i].count(' ') == 1:
                mas1.append(row[i])
            if row[i].count(' ') == 2:
                mas2.append(row[i])
            i+=1

counter = Counter(mas)
print("Самое часто встречающееся слово:", counter.most_common(1))
counter1 = Counter(mas1)
print("Самая часто встречающаяся пара слов:",counter1.most_common(1))
counter2 = Counter(mas2)
print("Самая часто встречающаяся тройка слов:",counter2.most_common(1))
input('Press ENTER to exit')