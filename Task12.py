# для натурального Н создать словарь
# индекс-значение, состоящий из элементов
# посл-ти 3н+1
# пример для н=6 :{1:4, 2:7, 3:10, 4:13, 5:16, 6:19}
from unittest import result


number = input('input integer N = ')
result=[]
for i in range(1, int(number)+1):
    elem = [i, 3*i+1]
    result.append(elem)
print(result)
print(dict(result))