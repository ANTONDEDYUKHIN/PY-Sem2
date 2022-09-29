# написать, программу, которая на вход принимает число
# и выдает последовательность из Н членов.
# напрмер: Н = 5: 1, -3, 9, -27, 81
numb = int(input('enter number N = '))
count = 0
res = 1
print(res)
for count in range(numb-1):
    res=res*-3
    count +=1
    print(res)