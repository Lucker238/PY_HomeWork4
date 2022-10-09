# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_factors(N):
    factors = [x for x in range(2,N) if N % x == 0]
    simp_factors = [x for x in factors if x == 2]
    for i in factors:
        for j in range(2,i):
            if i % j == 0:
                break
            elif j == i-1:
                simp_factors.append(i)        
    return(simp_factors)

print(find_factors(int(input('Введите число N: '))))
