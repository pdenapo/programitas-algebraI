def ejemplo(n):
 s=0
 for i in range (1,n+1):
 	s=s+(2*i-1)
 return s

for n in range(1,10):
 print("n=",n,"ejemplo(n)=",ejemplo(n))