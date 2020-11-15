# Sabiendo que el resto de la división de $a$ por 12 es 7, 
# calcular el resto de la división de $5a^2 + 38$ por 40.	

for q in countup(0,20):
    var a = 12 * q + 7
    var b = 5*a*a + 38
    var r = b mod 40
    echo "a = ",a," b = ",b," r = ",r
