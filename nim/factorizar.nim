

# Programa para factorizar un número en favtores primos - versión en nim

# Función que devuelve la factorización de un número n, como una lista de pares [d,e]
# donde d representa a cada uno de los factores primos del nùmero n y e es el exponente correspondiente 
   
# Nota: el código podrìa optimizarse mucho. No está pensado para ser eficiente, 
# sino para que sea fàcilde entender.
 
# Esta función factoriza un entero n y devuelve una secuencia de pares 
# en la forma [d,e] donde
# d es un divisor primo de n y e es el exponente correspondiente en su factorizaciòn */

import strutils

type
 factor_primo = tuple[primo:int, exponente: int] 

var
  factors_seq:seq[factor_primo]
  s: string
  numero:int

proc factorize(n0:int):seq[factor_primo]=
  var
    n,m,d,e: int
    p: factor_primo
    factors_seq=newSeq[factor_primo](0)
  # El parámetro p es inmutable, así que lo copiamos en una variable local.
  # En teoría, declararlo en var debería tener el mismo efecto pero no me funcionó.
  n=n0 
  for d in countup(2,n):
      e=0;  
      while n mod d == 0:
        e=e+1
        m=n div d
        echo(n,"=",m,"*",d)
        n=m
      if (e>0):
        p.primo = d
        p.exponente = e
        factors_seq.add(p)
  return factors_seq  

proc pretty_factorization(factors_seq:seq[factor_primo])=
    var
      already_printed= false
    if len(factors_seq)==0:
      write(stdout,"1")
    else:
     for p in factors_seq:
      if already_printed:
        write(stdout,"*")
      write(stdout,p.primo,"^",p.exponente)
      already_printed= true
    writeLine(stdout,"")

echo("Ingrese un número para factorizar")
s=readline(stdin)
numero=parseInt(s)
echo("Usted ingresó el número ",numero)
factors_seq=factorize(numero)
pretty_factorization(factors_seq)