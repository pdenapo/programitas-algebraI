#Progama en Python 3: aplicamos el algoritmo de Euclides a los números de
#Fibonacci (combinando los anteriores)

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
    print ("El algoritmo de Euclides termina")
    print ("El mcd es",a)
    return a
  else: 
   q, r= divmod(a,b)
   global pasos
   pasos=pasos+1
   print(a,"=",q,"*",b,"+",r)
   return mcd(b,r)

k=5
a=fibo(k+1)
b=fibo(k)
print("a=fibo(",k+1,")=",a)
print("b=fibo(",k,")=",b)
mcd(a,b)
print ("Tardamos ", pasos," pasos")

