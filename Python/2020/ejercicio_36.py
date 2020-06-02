
def f(n):
    return 3**n + 5**(n+1)

def g(n):
    return 3**(n+1) + 5**n

def mcd(a,b):
  if b>a:
   return mcd(b,a)
  if b==0:
    # print ("¡El algoritmo de Euclides termina!")
    # print ("El máximo común divisor es",a)
    return a
  else: 
   k, r= divmod(a,b)
   #print(a,"=",k,"*",b,"+",r)
   #print ("mcd(",a,",",b,")=mcd(",b,",",r,")")
   return mcd(b,r)

def h(n):
    return mcd(f(n),g(n))

for n in range(1,10):
  print("n=",n,"h(n)=",h(n))