
# Cálculo de las potencias del binomio usando Sage

var("x")
var("y")
b=x+y
Newton = 1 
for n in range(1,8):
 Newton= expand(Newton * b)
 print("(x+y)^"+str(n)+"&=",latex(Newton),"\\\\")