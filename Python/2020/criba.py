# Implementación en Python de la criba de Eratóstenes
# genera una tabla de los primos < que un limite dado

import argparse


def generar_criba(limite): 
    criba = dict()
    for n in range(2,limite):
        criba[n]=True
    p=2
    while p*p<=limite:
        print("p=",p)
        print(criba)
        # marcamos como compuestos a los múltiplos de p
        print("Tachamos los múltiplos de ",p)
        for n in range(p+1,limite):
            if n%p ==0:
                criba[n]=False
        # buscamos el número que siga a p en la
        # tabla que no haya sido marcado como compuesto.
        # necesariamente será primo (sino, sería divisible por un primo menor)
        encontramos_un_primo =False
        for n in range (p+1,limite):
            if criba[n]:
                p=n
                encontramos_un_primo=True
                print("nuevo p=",p)
                break;
        if not(encontramos_un_primo):
            print("No encontramos primos")
            break
    return criba

parser = argparse.ArgumentParser(description='Criba de Eratóstenes')
parser.add_argument("limite", type=int)
args=parser.parse_args()
criba=generar_criba(args.limite)
print("Criba final",criba)
