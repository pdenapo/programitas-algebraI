#!/usr/bin/env python3

#Progama en Python 3: aplicamos el algoritmo de Euclides a los números de
#Fibonacci (combinando los anteriores)

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

pasos=0

def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibo(n-1)+fibo(n-2)


def mcd(a,b):
  if b>a:
   return mcd(b,a)
  if b==0:
    print ("El algoritmo de Euclides termina!")
    print ("El máximo común divisor es",a)
    return a
  else: 
   q, r= divmod(a,b)
   global pasos
   pasos=pasos+1
   print(a,"=",q,"*",b,"+",r)
   return mcd(b,r)

parser = argparse.ArgumentParser(description='Calcula el máximo común divisor entre el k-ésimo  número de Fibonacci y el (k+1)-ésimo, usando el algoritmo de Euclides, y cuenta cuantos pasos tarda (es el peor caso!)')
parser.add_argument("k", type=int)
args=parser.parse_args()

a=fibo(args.k+1)
b=fibo(args.k)
print("a=fibo(",args.k+1,")=",a)
print("b=fibo(",args.k,")=",b)
mcd(a,b)
print ("Tardamos ", pasos," pasos")

