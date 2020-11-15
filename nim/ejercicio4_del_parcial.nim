
# Sea $\mathcal{F}$ el conjunto de todas las funciones 
# $\{1, 2, 3, 4, 5\} \rightarrow \{1, 2, . . . , 10\}$ que son estrictamente
#crecientes.
# a) ¿Cuántos elementos tiene el conjunto $\mathcal{F}$?

# Representamos cada una de las posibles funciones mediante un array
type
  IntArray = array[1..5, int] 

var f: IntArray

var cuantas:int =0 
for f1 in countup(1,10):
    for f2 in countup(f1+1,10):
        for f3 in countup(f2+1,10):
            for f4 in countup(f3+1,10):
                for f5 in countup(f4+1,10):
                    f[1]=f1
                    f[2]=f2 
                    f[3]=f3
                    f[4]=f4
                    f[5]=f5
                    echo f
                    inc(cuantas)

echo "Respuesta = ",cuantas 