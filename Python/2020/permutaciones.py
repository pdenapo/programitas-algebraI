# Genera una lista con todas las posibles permutaciones de una lista no vacía dada A
def permutaciones(A):
    # Variable para acumular los resultados
    resultado = []
    # Cuando la lista A sólo tiene un elmento x, generamos la lista [[x]]
    if len(A)==1:
        return [[A[0]]]
    else:
        for x in A:
            B = A.copy()
            B.remove(x)
            C = permutaciones(B)
            for y in C:
                z = y.copy()
                z.insert(0,x)
                resultado.append(z)
    return resultado  

def mostrar_permutaciones(A):
    p = permutaciones(A)
    print("Permutaciones de ",A,"=",p)
    print(len(p)," permutaciones en total.")


mostrar_permutaciones([1])
mostrar_permutaciones([1,2])
mostrar_permutaciones([1,2,3])
mostrar_permutaciones([1,2,3,4])
#mostrar_permutaciones([1,2,3,4,5])
#mostrar_permutaciones([1,2,3,4,5,6])