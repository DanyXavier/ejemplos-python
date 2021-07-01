# FORMA 1 : RECURSIVIDAD | NO OPTIMA
def fibonacciFun(n):
    if(n==0): return 0
    if(n==1): return 1
    return fibonacciFun(n-1) + fibonacciFun(n-2)

#size = 50
print("Serie infinita Fibonacci")
#for i in range(0,size):
#    print(f'{fibonacciFun(i)} ', end="")
#print()
#FORMA 2: ARRAY | OPTIMA

size = 150
fibonacci = []
fibonacci.append(0)
fibonacci.append(1)
for i in range(0,size):
    if i>1:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(f'{fibonacci[i]} ',end="")
print()