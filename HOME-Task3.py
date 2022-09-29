#Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from unittest import result


number = input('input integer N = ')
result=[]
count=4
for i in range(1, int(number)+1):
    elem = [i, count]
    count+=3
    result.append(elem)

print(dict(result))