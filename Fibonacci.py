#Progama en Python 3 que genera la tabla de los números de Fibonacci

def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

for k in range(0,16):
  print ("fibo(",k,")=",fibo(k))