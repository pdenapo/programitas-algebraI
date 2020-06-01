# suma del ejercicio 25 ii) de la práctica 3
import scipy
from scipy import special 
from scipy.special import binom

def s(n):
    return sum([scipy.special.binom(2*n+1,k) for k in range(0,n+1)])

for n in range (1,10):
  print ("n=",n,"s(n)=",s(n),"nos dio=", 2**(2*n))
