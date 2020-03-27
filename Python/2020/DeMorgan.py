# Progrma para chequear la validez de una de las leyes de De Morgan
# \neg (p \vee q) \Leftrightarrow \neg p \wedge \neg q 
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
def equivalence(p,q):
  return imp(p,q) and imp (q,p)

valores_de_verdad = [True,False]
print("\\begin{array}{|l|l|l|l|l|l|l|l|}")
print("\\hline")
print("p & q & p \\vee q & \\neg(p \\vee g) & \\neg p & \\neg q & \\neg p \\wedge \\neg q & T \\\\")
print("\\hline")
for p in valores_de_verdad:
 for q in valores_de_verdad:
  r= not(p or q)
  s = not(p) and not(q)
  print(nombre(p) ,"&", nombre(q), "&", nombre(p or q), "&", nombre(r) ,"&", nombre(not(p)),"&",nombre(not(q)),"&", nombre(s),"&", nombre(equivalence(r,s)), "\\\\") 
print("\\hline")
print("\\end{array}") 