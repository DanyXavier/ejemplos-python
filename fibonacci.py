# 0 1 1 2 ... n
# n = n-1 + n-2
# SERIE FIBONACCI
#FORMA 1 : RECURSIVIDAD | NO OPTIMA
def fibonacci(n):
    if (n==0): return 0
    if (n==1): return 1
    return fibonacci(n-1) + fibonacci(n-2)
#longitud = 100 # 4 elementos
#for i in range(0,longitud):
#    print(f'{fibonacci(i)} ',end="")
#print()

# SERIE FIBONACCI
#FORMA 2: ARRAY
longitud = 100
fibonacc = []
fibonacc.append(0)
fibonacc.append(1)
for i in range(0,longitud):
    if i> 1:
        # n = n-1 + n-2
        fibonacc.append(fibonacc[i-1] + fibonacc[i-2])
    print(f'{fibonacc[i]} ',end='')
print()
