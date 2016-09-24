#!/usr/bin/env python3

#Progama en Python 3 que genera la tabla de los números de Fibonacci

# Programa en Python 3 que calcula el máximo común divisor 
# usando el algoritmo de Euclides, y los coeficientes que permiten 
# escribirlo como combinación lineal

# Este programa tiene solamente propósitos didácticos 
# (es para mis alumnos de Algebra I).

# (C) 20014-2016  Pablo De Nápoli <pdenapo@dm.uba.ar>

# Este programa es software libre, y usted puede redistribuirlo o 
# modificarlo libremente bajo los términos de la 
# GNU General Public Licence (Licencia Pública General), versión 3
# o cualquier versión posterior, 
# publicada por la Free Software Foundation. Vea:
#
# http://www.gnu.org/copyleft/gpl.html

import argparse

def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)

parser = argparse.ArgumentParser(description='Calcula la tabla de los números de Fibonacci hasta la tala de los números de Fibonacci hasta un lugar dado')
parser.add_argument("hasta", type=int)
args=parser.parse_args()


for k in range(0,args.hasta+1):
  print ("fibo(",k,")=",fibo(k))
