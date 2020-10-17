
import sys
import numpy as np
from math import gcd

def chequea_invariante(a,b,m):
  if not(a*m[0,0]+ b*m[0,1] ==m[0,2]):
    sys.exit("¡La primera ecuación no se cumple!")
  if not(a*m[0,0]+ b*m[0,1] ==m[0,2]):
    sys.exit("¡La segunda ecuación no se cumple!")
  if not(gcd(a,b)==gcd(m[0,2],m[1,2])):
     sys.exit("El máximo común divisor no se preserva") 

def Euclides_extendido(a,b):
    paso =0
    m=np.array([[1,0,a],[0,1,b]])
    while True:
        #print("paso ",paso)
        paso=paso+1
        #print(m)  
        if m[0,2]==0:
            # Si se llega a un cero, el algoritmo termina y devuelve el mcd y los coeficientes de la 
            # combinación lineal
            mcd_a_b=m[1,2]
            s_a_b = m[1,0]
            t_a_b = m[1,1]
            break
        elif m[1,2]==0:
            mcd_a_b=m[0,2]
            s_a_b = m[0,0]
            t_a_b = m[0,1]
            break
        elif m[0,2] >= m[1,2]:
            q,r=divmod(m[0,2],m[1,2])
            # Restamos a la primer fila q veces la segunda
            m[0,0] = m[0,0] - q*m[1,0]
            m[0,1] = m[0,1] - q*m[1,1]
            m[0,2] = r
        else:
            q,r=divmod(m[1,2],m[0,2])
            # Restamos a la segunda fila q veces la primera
            m[1,0] = m[1,0] - q*m[0,0]
            m[1,1] = m[1,1] - q*m[0,1]
            m[1,2] = r
        chequea_invariante(a,b,m)
    return (s_a_b,t_a_b,mcd_a_b)

def tabla0():
    for n in range(0,30):
        if n% 5==0:
            print("n=",n)
            a=n**2+1
            b=n+2
            s,t,mcd= Euclides_extendido(a,b)
            q = n//5
            if a==25*q**2+1:
                print("a OK")
            if b==5*q+2:
                print("b OK")
            mi_s = 2*q+1
            mi_t = -(10*q+1)*q  
            print(n,"&",n // 5, "&",a, "&",b,"&",s,"&",t,"&",mcd,"\\\\")
            if s==mi_s:
                print("s OK")
            else:
                print("s errado")
            if t==mi_t:
                print("t OK")
            else:
                print("t errado t=",t,"mi_t=",mi_t)      



def tabla1():
    for n in range(0,30):
        if n% 5==1:
            print("n=",n)
            a=n**2+1
            b=n+2
            s,t,mcd= Euclides_extendido(a,b)
            q = n//5
            if a==25*q**2+10*q+2:
                print("a OK")
            if b==5*q+3:
                print("b OK")
            mi_s = -(2*q+1)
            mi_t = 10*q**2+3*q+1  
            print(n,"&",n // 5, "&",a, "&",b,"&",s,"&",t,"&",mi_t, "&",mcd,"\\\\")
            if s==mi_s:
                print("s OK")
            if t==mi_t:
                print("t OK")                      