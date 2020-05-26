# Ejercicio 10 item c) práctica 4

def factorial(n):
    if n== 1:
        return 1
    else:
        return n*factorial(n-1)

def s(n):
    return sum([(-1)**i * factorial(i) for i in range(1,n+1)])

for n in range(1,11):
    s1 = s(n)
    s2 = s1 % 36
    print ("n= ",n,"s(n)=",s1," s(n) módulo 36 =", s2)            