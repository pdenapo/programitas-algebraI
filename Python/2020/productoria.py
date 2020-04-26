def factorial(n):
 p=1
 for k in range (1,n+1):
 	p=p*k
 return p

for n in range(1,10):
 print("n=",n,"factorial(n)=",factorial(n))