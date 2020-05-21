
# Implementación recursiva de los combinatorios en Python 3
def combinatorio(n,k):
    if k==0:
        return 0 
    elif k==n: 
      return 1
    else:
      return combinatorio(n-1,k)+combinatorio(n-1,k-1)


for n in range (0,10):
    for k in range(0,n+1):
      print("combinatorio(",n,",",k,")=",combinatorio(n,k))