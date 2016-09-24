# Programa en Python 3 que calcula el máximo común divisor 
# usando el algoritmo de Euclides, y los coeficientes que permiten 
# escribirlo como combinación lineal


def chequea_invariante(a,b,alfa_a_b,beta_a_b,mcd_a_b):
 # chequea el invariante del algoritmo 
  print("alfa(",a,",",b,")=",alfa_a_b,end=', ')
  print("beta(",a,",",b,")=",beta_a_b,end=', ')
  print("mcd(",a,",",b,")=",mcd_a_b)
  print(mcd_a_b,"=",alfa_a_b,"*",a,"+",beta_a_b,"*",b)
  


def ecl(a,b):
  if b>a:
   return ecl(b,a)
  if b==0:
      alfa_a_b=1
      beta_a_b=0
      mcd_a_b=a
  else: 
     q,r=divmod(a,b)
     alfa_b_r, beta_b_r, mcd_b_r = ecl(b,r) 
     alfa_a_b =  beta_b_r
     beta_a_b = alfa_b_r - beta_b_r * q
     mcd_a_b = mcd_b_r
  chequea_invariante (a,b,alfa_a_b,beta_a_b,mcd_a_b)
  return (alfa_a_b,beta_a_b,mcd_a_b)
  

ecl(360,28)