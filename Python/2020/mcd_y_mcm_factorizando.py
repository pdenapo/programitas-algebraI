

import argparse 
import sys

def exponente(n,d):
    """ Dados d y n calcula el máximo exponente de d que divide a n
        Si d es primo, es el exponente factorización de n
        (valuación p-ádica)
        devuelve: (e,m) donde e es el exponente e y  m=n/d^e"""
    q,r = divmod(n,d)
    if r == 0:
      e1,m =  exponente(q,d)
      # q = n/d = d^{e_1} * m 
      # => n = d^{e_1+1} * m
      e = e1 + 1 
    else: 
      e = 0
      m = n 
    #print("exponente(",n,",",d,")=",(e,m))
    # Chequeamos el invariante n= m* d^e
    if not(n == m*d**e):
       sys.exit("¡No se cumple!")
    return e,m 

def calcular_producto(l):
    """ Dada una lista de pares de la forma (p,e) calcula el producto de los valores p^d"""
    p=1
    for f in l:
      p=p*f[0]**f[1]
    return p  


def factorizar(n):
    """# Factoriza n en primos. Devuelve una lista de pares (p,e) de primos y exponentes
    El invariante es: n es igual al producto de los primos a los exponentes"""
    lista = [] 
    if n>1:
        # Miramos los divisores hasta la raiz cuadrada
        # El primer divisor que encontramos debe ser un primo
        # Ahi calculamos el exponente y salimos del ciclo
        d=1 
        while d*d <=n:
            d=d+1
            e,m = exponente(n,d)
            if e>0:
                lista = [(d,e)]
                lista= lista + factorizar(m)
                break 
        # Si la lista está vacía (no encontramos ningún factor), es porque n era primo
        if not lista:
            lista = [(n,1)]
    # print("factorizar(",n,")=",lista)
    # Chequeamos el invariante n= m* d^e
    if not(type(lista))== list:
        sys.exit("El resultado de factorizar debe ser una lista")
    if not(n == calcular_producto(lista)):
        sys.exit("¡No se cumple!")        
    return lista

def mostrar_lindo(l):
    """Muestra una factorización calculada en forma linda (producto de factores p^e) """
    hay_un_factor= False
    for f in l:
       if hay_un_factor:
         print(" * ",end="")
       print(f[0],"^",f[1],end="",sep='')
       hay_un_factor=True
    print("\n")

def busca_exponente(p,l):
    """busca el exponente de un primo en una factorización dada"""
    for f in l:
        if f[0]==p:
           return f[1]
    # si llegamos acá, el primo no aparece en la factorización dada
    return 0


def mcd_Euclides(a,b):
  """Calcula el máximo común divisor por el alogitmo de Euclides. Lo usamos como
  comprobación. """
  if b>a:
   return mcd_Euclides(b,a)
  if b==0:
    return a
  else: 
   k, r= divmod(a,b)
   return mcd_Euclides(b,r)

def factorizacion_mcd(fa,fb):
    """Calcula la factorización del mcd de a y b a partir de las factorizaciones de a y de b."""
    resultado=[]
    for f in fa:
      p = f[0] # El primo
      ea = f[1] # el exponente en la factorización 
      eb = busca_exponente(p,fb) # el exponente en la otra factorización
      # si el exponente es positivo, el primo aparece en ambas factorizaciones
      # entonces calculamos el exponente en el mcd y lo agregamos
      if eb>0:
              resultado.append((p,min(ea,eb)))
    return resultado

def listar_primos(fa):
    """Lista los primos que aparecen en una factorización dada"""
    resultado=[]
    for f in fa:
      resultado.append(f[0])
    return resultado

def unicos(lista):
    """Obtener una lista sin valores repetidos a partir de una dada."""
    resultado = [] 
    for x in lista: 
        if x not in resultado: 
            resultado.append(x) 
    return resultado

def factorizacion_mcm(fa,fb):
    """Calcula la factorización del mcm de a y b a partir de las factorizaciones de a y de b."""
    resultado=[]
    todos_los_primos = listar_primos(fa) + listar_primos(fb)
    todos_los_primos = unicos(todos_los_primos)
    todos_los_primos.sort()

    for p in todos_los_primos:
        ea = busca_exponente(p,fa) # el exponente en la factorización 
        eb = busca_exponente(p,fb) # el exponente en la otra factorización
        resultado.append((p,max(ea,eb)))
    return resultado

if __name__ == "__main__":
    # Parte principal del programa. Leemos los argumentos
    parser = argparse.ArgumentParser(description='Calcula el máximo común divisor y el máximo común múltiplo factorizando.')
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args=parser.parse_args()

    print("Calculamos el máximo común divisor y el mínimo común múltiplo entre ",args.a," y ",args.b," usando sus factorizaciones \n")   
    # factorizamos a y b
    fa = factorizar(args.a)
    fb = factorizar(args.b)
    print(args.a,"=",end="")
    mostrar_lindo(fa)
    print(args.b,"=",end="")
    mostrar_lindo(fb) 
    # Calculamos el mcd factorizando  
    fmcd= factorizacion_mcd(fa,fb)
    mcd = calcular_producto(fmcd)
    # Chequeamos el resultado con el que da el algoritmo de Euclides
    if not(mcd == mcd_Euclides(args.a,args.b)):
        sys.exit("El mcd no fue correctamente calculado")        
    print("mcd =",mcd,end=" = ")
    mostrar_lindo(fmcd)
    fmcm= factorizacion_mcm(fa,fb)
    # Calculamos el mcm factorizando
    mcm=calcular_producto(fmcm)
    # Chequeamos el resultado con el obtenido a partir del mcd
    if not(mcm == args.a*args.b/mcd):
        sys.exit("El mcm no fue correctamente calculado")        
    print("mcm =",calcular_producto(fmcm),end=" = ")
    mostrar_lindo(fmcm)

