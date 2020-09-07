# Progrma para chequear la validez de la fórmula 
# (p -> q) <-> ( p \ )
# mediante una tabla de verdad.
# salida: Una tabla en LaTeX

# Nombres de los valores de verdad en castellano
def nombre(x):
 if x: 
  return "1"
 else:
  return "0"

# Implicación
def imp(p,q):
 return not(p) or q 

# Equivalencia Lógica
def equivalencia(p,q):
  return imp(p,q) and imp (q,p)

valores_de_verdad = [False,True]
print("\\begin{array}{|l|l|l|l|l|l|l}")
print("\\hline")
print("p & q & p \\  NOT(p) & p AND q & p OR q & p XOR q \\\\")
print("\\hline")
for p in valores_de_verdad:
 for q in valores_de_verdad:
    print(nombre(p) ,"&", nombre(q),"&", nombre(not(p)), "&", nombre(p and q), "&", nombre(p or q) ,"&", nombre(p^q),"\\\\") 
print("\\hline")
print("\\end{array}") 