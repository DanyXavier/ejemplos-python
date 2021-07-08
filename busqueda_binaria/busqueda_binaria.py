#FORMA 1 : RECURSIVIDAD
#MÉTODO RECURSIVO
def findIndex(array,target,min,max):
    guess = int((min+max)/2)
    if array[guess] == target:
        return guess
    elif (array[guess] < target):
        return findIndex(array,target,guess+1,max)
    else:
        return findIndex(array,target,min,guess-1)

# lista ordenada o ordenar la lista de mayor a menor
array = [3,5,8,13,19,21,25,26,28,32,39,41,50,54,69]
target = 26
min= 0
max = len(array) - 1
#FORMA 1 : RECURSIVIDAD
index = findIndex(array,target,min,max)
print(f'El valor objetivo {target} esta en el indice de mi array {index} y su valor es: {array[index]}')
print()
print()
#FORMA 2 : BUCLE
while(True):
    guess = int((min+max)/2)
    if array[guess] == target:
        print(f'El valor de mi variable objetivo {target} esta en el indice de mi array {guess} y su valor es: {array[guess]}')
        break
    elif (array[guess]<target):
        min = guess + 1
    else:
        max = guess - 1

