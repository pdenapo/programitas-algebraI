
# Dados d y n calcula el máximo exponente de d que divide a n
# Si d es primo, es el exponente factorización de n
# (valuación p-ádica)
# devuelve: el exponente e y el número m=n/d^e

import argparse 
import sys

def exponente(n,d):
    q,r = divmod(n,d)
    if r == 0:
      e1,m =  exponente(q,d)
      # q = n/d = d^{e_1} * m 
      # => n = d^{e_1+1} * m
      e = e1 + 1 
    else: 
      e = 0
      m = n 
    print("exponente(",n,",",d,")=",(e,m))
    # Chequeamos el invariante n= m* d^e
    if not(n == m*d**e):
       sys.exit("¡No se cumple!")
    return e,m 

# Factoriza n en primos. 
# Devuelve una lista de pares (p,e) de primos y exponentes
# El invariante es: n es igual al producto de los primos a los exponentes

def factorizar(n):
  if n==1:
    return []
  # Miramos los divisores hasta la raiz cuadrada
  # El primer divisor que encontramos debe ser un primo
  # Ahi calculamos el exponente y salimos del ciclo
  d=1 
  lista =[]
  while d*d <=n:
    d=d+1
    e,m = exponente(n,d)
    if e>0:
      lista = [(d,e)]
      lista= lista + factorizar(m)
      print("factorizar(",n,")=",lista)
      # Acá salimos de la función, el ciclo se acaba.
      return lista
  # Si llegamos hasta acá (encontramos ningún factor), es porque n era primo
  return [(n,1)]    
   
    
def factorizar_lindo(n):
    l = factorizar(n)
    hay_un_factor= False
    for f in l:
       if hay_un_factor:
         print("*",end="")
       print(f[0],"^",f[1],end="")
       hay_un_factor=True
    print("\n")

parser = argparse.ArgumentParser(description='Calcula la factorización en primos de un entero n')
parser.add_argument("n", type=int)
args=parser.parse_args()
factorizar_lindo(args.n)    
