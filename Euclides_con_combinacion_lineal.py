#!/usr/bin/env python3

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

def chequea_invariante(a,b,alfa_a_b,beta_a_b,mcd_a_b):
 # chequea el invariante del algoritmo 
  print("alfa(",a,",",b,")=",alfa_a_b,end=', ')
  print("beta(",a,",",b,")=",beta_a_b,end=', ')
  print("mcd(",a,",",b,")=",mcd_a_b)
  print(mcd_a_b,"=",alfa_a_b,"*",a,"+",beta_a_b,"*",b)
  
def mcd_con_combinacion_lineal(a,b):
  if b>a:
   return mcd_con_combinacion_lineal(b,a)
  if b==0:
      alfa_a_b=1
      beta_a_b=0
      mcd_a_b=a
  else: 
     q,r=divmod(a,b)
     alfa_b_r, beta_b_r, mcd_b_r = mcd_con_combinacion_lineal(b,r) 
     alfa_a_b =  beta_b_r
     beta_a_b = alfa_b_r - beta_b_r * q
     mcd_a_b = mcd_b_r
  chequea_invariante (a,b,alfa_a_b,beta_a_b,mcd_a_b)
  return (alfa_a_b,beta_a_b,mcd_a_b)
  
parser = argparse.ArgumentParser(description='Calcula el máximo común divisor usando el algoritmo de Euclides y lo escibe como una combinación lineal')
parser.add_argument("a", type=int)
parser.add_argument("b", type=int)
args=parser.parse_args()

print("Calculamos el máximo común divisor entre ",args.a," y ",args.b)   
mcd_con_combinacion_lineal(args.a,args.b)
