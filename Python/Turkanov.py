# Implementación en Python 3 de la fórmula de Igor Turkanov 
# para contar primos
# http://arxiv.org/abs/1603.02914
# Por Pablo De Nápoli <pdenapo@gmail.com> - Licencia: GPL versión 3

from fractions import gcd
from math import floor,sqrt

# Esta función genera una lista cuyos elementos son todas
# las posibles listas [i_1,i_2_...,i_s]
# con 1 < i_1<i_2 < ... < i_s <= k
def generar_lista(s,k):
   L=[]
   for i in range(2,k+1):
    if s==1:
     L.append([i])
    else:
     M=generar_lista(s-1,i-1)
     for e in M:
      f=e
      f.append(i)
      L.append(f)
   return L

# Esta función calcula el mìnimo comùn mùltiplo de dos enteros
def lcm(n,m):
    return n*m//gcd(n,m) 
    
# Esta función calcula el mìnimo comùn múltiplo de los elementos de 
# una lista de enteros    
def lcm_lista(L):
    if len(L)==1:
      return L[0]
    else:
      return lcm(lcm_lista(L[:-1]),L[-1])

# Esta función calcula la cantidad de primos <= n 
# mediante la fòrmula de Igor Turkanov          
def primes_pi(n):
    pi=n-1
    limite=floor(sqrt(n))
    for i in range(2,limite+1):
     pi=pi-(n//i-i+1)
    for s in range(2,limite+1):
     L=generar_lista(s,limite)
     t=0
     for I in L:
      lcm_I = lcm_lista(I)
      t=t+n//lcm_I - (I[-1]**2-1)//lcm_I
     if s%2==0:
      pi=pi+t
     else:
      pi=pi-t 
    return pi


# Esta función imprime una tabla de la función primes_pi 
# hasta el límite solicitado
def imprimir_tabla(limite):    
  for k in range(2,limite+1):
    print(k," ",primes_pi(k))
   
imprimir_tabla(100)