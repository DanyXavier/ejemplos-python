"""
[5,4,9]
tamaño : 3
indice a cambiar: 0
elemento del indice a cambiar: 5
hacer comparaciones ara intercambiar los valores
nuevo indice : 1
nuevo elemento de ese indic: 4
[4,5,9]
"""
array = [10,7,3,13,2,50,3,10,2,1,7,0] # array con elemntos númericos
print(f'Array inicial {array}')
# tomar un elemento a la vez y compararlo para intercambiarlo con un nuevo menor
for i in range(0,len(array)):
    minValue = array[i] # elemento seleccionado a itercambiar para compararlo si es que no existe un valor mas pequeño 
    minIndex = i # la posicion donde esta ubicado el elemento a intercambiar
    #for j,el in enumerate(array)
    for j in range(minIndex+1,len(array)):
        if array[j] < minValue:
            minValue = array[j]
            minIndex = j
    temp = array[i] # 10
    array[i] = minValue # [2,7,3,13,2] i= 0 minValue = 2 temp = 10
    array[minIndex] = temp # minIndex = 4 temp = 10 #[2,7,3,13,10]

print(f'Array final {array}')
