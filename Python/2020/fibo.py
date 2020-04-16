#Progama en Python 3 que genera la tabla de los números de Fibonacci
#y comprueba las fórmulas de la clase sobre inducción.

def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

def S(n):
    if n==1:
        return fibo(1)
    else: 
        return S(n-1)+fibo(n)

def comprobar(n):
    return S(n)== fibo(n+2)-1 

def comprobar_gaussianos(n):
    return fibo(n)**2+ fibo(n+1)**2 == fibo(2*n+1)

# Acá pueden usar la función comprobar_gaussianos si quieren comprobar
# la fórmula de @gaussianos
for n in range(1,10):
  print("n=",n," comprobar(n)=",comprobar(n))