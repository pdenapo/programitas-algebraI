#!/usr/bin/env python3

# Programa en Python 3 que calcula el máximo común divisor 
# usando el algoritmo de Euclides, y los coeficientes que permiten 
# escribirlo como combinación lineal

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

import argparse
import sys

def chequea_invariante(a,b,s_a_b,t_a_b,mcd_a_b):
 # chequea el invariante del algoritmo 
  print("s(",a,",",b,")=",s_a_b,end=', ')
  print("t(",a,",",b,")=",t_a_b,end=', ')
  print("mcd(",a,",",b,")=",mcd_a_b)
  print(mcd_a_b,"=",s_a_b,"*",a,"+",t_a_b,"*",b)
  if not(s_a_b *a + t_a_b * b == mcd_a_b):
    sys.exit("¡No se cumple!")
   

def mcd_con_combinacion_lineal(a,b):
  if b>a:
   s,t,d=mcd_con_combinacion_lineal(b,a)
   return (t,s,d)
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
  chequea_invariante (a,b,s_a_b,t_a_b,mcd_a_b)
  return (s_a_b,t_a_b,mcd_a_b)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Calcula el máximo común divisor usando el algoritmo de Euclides y lo escibe como una combinación lineal')
  parser.add_argument("a", type=int)
  parser.add_argument("b", type=int)
  args=parser.parse_args()

  print("Calculamos el máximo común divisor entre ",args.a," y ",args.b)   
  mcd_con_combinacion_lineal(args.a,args.b)
