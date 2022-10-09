# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
#  элементов исходной последовательности.
import random

def create_massiv():
    length = int(input('Введите длину последовательности: '))
    result = []
    while len(result) < length:
        result.append(random.randint(1,9))
    return result

massiv = create_massiv()
sorted_massiv = [x for x in massiv if massiv.count(x) < 2]

print(massiv)
print(sorted_massiv)