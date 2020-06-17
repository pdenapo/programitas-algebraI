# Resolvemos una ecuación diofántica en Python 3

import matplotlib.pyplot as plt
import numpy as np
import argparse 
import sys

def dibuja_diofántica(a,b,c):
    # definimos el tamaño de la imagen
    plt.figure(figsize=(10,10))
    # Agregamos los ejes y ponemos marcas en los enteros
    plt.axvline()
    plt.axhline()
    plt.xticks(range(-10,11))
    plt.yticks(range(-10,11))
    # dibujamos el retítulo de coordenadas enteras
    for x in range(-10,11):
        for y in range(-10,11):
            plt.plot(x,y,"ro",markersize=3)
    x = np.linspace(-10,10)
    # ax+by=c <=> by= c-ax <=> y=c/b - (a/b)*x
    y = (c/b) - (a/b)*x
            
    s,t,d = mcd_con_combinacion_lineal(a,b)
    # d es el máximo común divisor de a y b, sa+tb=d
    if not(s *a + t* b == d):
        sys.exit("¡No se cumple!")
  
    q,r = divmod(c,d)
    if r==0:
    # Encontramos una solución particular
       x0= q*s
       y0= q*t 
       plt.plot(x0,y0,"bo")
       solución = "Una solución particular es ("+str(x0)+","+str(y0)+")"
    plt.plot(x,y,"g",label="La ecuación diofántica "+str(a)+"*x+"+str(b)+"*y="+str(c)+"\n"+solución)
    legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C0')
    plt.show()


def mcd_con_combinacion_lineal(a,b):
  if b==0:
      s_a_b=1
      t_a_b=0
      mcd_a_b = a
  else: 
     k,r=divmod(a,b)
     s_b_r, t_b_r, mcd_b_r = mcd_con_combinacion_lineal(b,r) 
     s_a_b =  t_b_r
     t_a_b = s_b_r - k*t_b_r 
     mcd_a_b = mcd_b_r
  return (s_a_b,t_a_b,mcd_a_b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dibuja la ecuación diofántica ax+by=c')
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("c", type=int)
    args=parser.parse_args()
    dibuja_diofántica(args.a,args.b,args.c)
