# EJEMPLO 1 FACTORIAL
# 3! = 3*2*1 = 6        n...*1
def factorial(n):
    if(n==1):
        return 1
    else:
        return factorial(n-1)*n
# f(3)
# 3==1 ? 1 : f(3-1) * 3
# f(2)
# 2== 1? 1 : f(2-1) * 2
# f(1)
# 1==1 ? 1
# 1*2*3 return 6
#n = int(input("Ingrese un número para el cálculo del factorial \n"))
#print(f'El numero del factorial es {n} es igual a: { factorial(n)}')

#EJEMPLO 2 LECTURA DE ARRAY

def readArray(array,index):
    if(array.__len__() != index):
        print(f'el elemento {array[index]} esta en el index {index}')
        readArray(array,index+1)

# 4
# ar({1,2,3,4},0)
# 4!= 0 ?  ar({1,2,3,4},0+1)
# 4!=1 ? ar({1,2,3,4},1+1)
array = [1,2,3,4,5]
array.reverse()
# aleatorea
readArray(array,0)