#!/usr/bin/env python3

# Programa en Python 3 que calcula el máximo común divisor 
# usando la versión matricial del algoritmo de Euclides, y los coeficientes que permiten 
# escribirlo como combinación lineal
# según el artículo de Antonio Cafure
# "El algoritmo de Euclides y la Noción de divisor común máximo"

# Este programa tiene solamente propósitos didácticos 
# (es para mis alumnos de Algebra I).

# (C) 20014-2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

# Este programa es software libre, y usted puede redistribuirlo o 
# modificarlo libremente bajo los términos de la 
# GNU General Public Licence (Licencia Pública General), versión 3
# o cualquier versión posterior, 
# publicada por la Free Software Foundation. Vea:
#
# http://www.gnu.org/copyleft/gpl.html

#import argparse
import sys
#import numpy as np

def chequea_invariante(a,b,m):
  if not(a*m[0,0]+ b*m[0,1] ==m[0,2]):
    sys.exit("¡La primera ecuación no se cumple!")
  if not(a*m[0,0]+ b*m[0,1] ==m[0,2]):
    sys.exit("¡La segunda ecuación no se cumple!")
  if not(gcd(a,b)==gcd(m[0,2],m[1,2])):
     sys.exit("El máximo común divisor no se preserva") 

def Euclides_extendido(a,b):
    paso =0
    m=matrix([[1,0,a],[0,1,b]])
    while True:
        paso=paso+1
        print("paso ",paso,"\n",m) 
        if m[0,2]==0:
            mcd =m[1,2]
            s = m[1,0]
            t = m[1,1]
            break
        elif m[1,2]==0:
            mcd=m[0,2]
            s = m[0,0]
            t = m[0,1]
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
    return (s,t,mcd)

