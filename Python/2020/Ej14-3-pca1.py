# Progrma para chequear la validez de la fórmula del ejercicio 14 iii) de la práctica 1
# mediante una tabla de verdad.
# salida: Una tabla en LaTeX

# Nombres de los valores de verdad en castellano
def nombre(x):
 if x: 
  return "V"
 else:
  return "F"

# Implicación
def imp(p,q):
 return not(p) or q 

# Equivalencia Lógica
def equivalencia(p,q):
  return imp(p,q) and imp (q,p)

valores_de_verdad = [True,False]
print("\\begin{array}{|l|l|l|l|l|l|l}")
print("\\hline")
print("p & q & p \\veebar q & \sim(p \\vee g) & p \wedge  \sim(p \\veebar q)  & T \\\\")
print("\\hline")
for p in valores_de_verdad:
 for q in valores_de_verdad:
    r = p ^ q 
    s = not(r)
    u = p & s
    v = p & q  
    t = equivalencia(u,v)
    print(nombre(p) ,"&", nombre(q), "&", nombre(r), "&", nombre(s) ,"&", nombre(u),"&",nombre(v),"&", nombre(t), "\\\\") 
print("\\hline")
print("\\end{array}") 