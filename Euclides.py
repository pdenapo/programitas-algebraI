# Programa recursivo en Python 3 para calcular el máximo común divisor
# usando el algoritmo de Euclides

def mcd(a,b):
  if b>a:
   return mcd(b,a)
  if b==0:
    print ("El algoritmo de Euclides termina")
    print ("El mcd es",a)
    return a
  else: 
   q, r= divmod(a,b)
   print(a,"=",q,"*",b,"+",r)
   return mcd(b,r)
   
mcd(360,28)