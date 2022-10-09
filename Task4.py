# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }

def create_polynomial(k):
    result = [''] * (k+1)
    index = 0
    while k >= 0:
        rand = random.randint(0,9)
        if rand == 0:
            result.pop()
            index -= 1
            continue
        elif rand == 1:
            result[index] = 'x'
        else:
            result[index] = str(rand) + 'x'  
        if k > 1:
            for simb in str(k):
                result[index] += indexes[simb]
        elif k == 1:
            if rand == 1:
                result[index] = 'x'
            else:
                result[index] = str(rand) + 'x'
        else:
            result[index] = str(rand)
        index += 1
        k -= 1
    return ' + '.join(map(str,result))


print(create_polynomial(int(input('Введите длину полинома: '))))
