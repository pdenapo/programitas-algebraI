
  # Elevamos a la potencia k usando cuadrados repetidos
  # guardamos el resultado

def elevar(a,k):
  if k==0:
    b=1 
  elif k==1:
    b=a
  else:
    q, r = divmod(k, 2)
    print (k,"=2*",q,"+",r)
    if r==0:
        b= elevar(a,q)**2
    else:
        b= elevar(a,q)**2*a
  print(a,"**",k,"=",b)
  return b

def elevar_modulo_n(a,k,n):
  if k==0:
    b=1 
  elif k==1:
    b=a
  else:
    q, r = divmod(k, 2)
    print (k,"=2*",q,"+",r)
    if r==0:
        b= elevar_modulo_n(a,q,n)**2
    else:
        b= elevar_modulo_n(a,q,n)**2*a
  b = b % n
  print(a,"**",k,"=",b,"(módulo ",n,")")
  return b


#print (elevar(2,31))
#print (elevar(2,51833))
print (elevar_modulo_n(2,51833,31))