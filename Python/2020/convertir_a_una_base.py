def digitos(n,b):
    if n<b:
       return [n]
    else:
        q,r= divmod(n,b)
        d = digitos(q,b) 
        d.append(r)
        print("d=",d)
        return d

print(digitos(15151,16))