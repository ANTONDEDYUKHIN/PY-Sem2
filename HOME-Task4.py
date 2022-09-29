# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
# ГДЕ ВЗЯТЬ ФАЙЛ ТХТ?
result=[]
n = int(input('enter number N ='))
i = -n
while i<n:
    i+=1
    elem=i
    result.append(elem)
print(result, end=' ')