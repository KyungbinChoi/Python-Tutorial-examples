#LAB_04_04

def Fib(n):
    if n==1:return 1
    elif n==2: return 2
    return Fib(n-1) + Fib(n-2) #Recursion

n = int(input("Enter a positive number: "))
print(Fib(n))

