"""
[9,5,7,2,4,1]
primer indice = 0
valor = 9
elemento mas bajo = 1
indice = 5
intercambio
primer indice = 0
valor 1
[1,5,7,2,4,9]
primer indice = 1
valor = 5
[1,2,7,5,4,9]
"""
array = [10,7,3,13,2,15,6,19,3]
print(f'array incial {array}')
for indice,elemento in enumerate(array):
    minValue = elemento
    minIndex = indice
    for j in range(minIndex + 1,len(array)):
        if array[j] < minValue:
            minValue = array[j]
            minIndex = j
    temp = array[indice] # 10 
    array[indice] = minValue # [2,7,3,13,2]
    array[minIndex] = temp # [2,7,3,13,10]
print(f'array final {array}')
