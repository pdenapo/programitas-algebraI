#!/usr/bin/env python3

# Programa recursivo en Python 3 para calcular el máximo común divisor
# usando el algoritmo de Euclides

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

def mcd(a,b):
  if b>a:
   return mcd(b,a)
  if b==0:
    print ("¡El algoritmo de Euclides termina!")
    print ("El máximo común divisor es",a)
    return a
  else: 
   k, r= divmod(a,b)
   print(a,"=",k,"*",b,"+",r)
   print ("mcd(",a,",",b,")=mcd(",b,",",r,")")
   return mcd(b,r)

parser = argparse.ArgumentParser(description='Calcula el máximo común divisor usando el algoritmo de Euclides')
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)
args=parser.parse_args()

print("Calculamos el máximo común divisor entre ",args.a," y ",args.b)   
mcd(args.a,args.b)
