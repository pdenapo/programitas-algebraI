

/* Programa para factorizar un número en favtores primos 
- Versión en lenguaje D  

   Nota: el código podrìa optimizarse mucho. No está pensado para ser eficiente, sino para que sea fàcil
   de entender.
 */


/* Esta función factoriza un entero n y devuelve una lista de pares en un array en la forma [d,e] donde
d es un divisor primo de n y e es el exponente correspondiente en su factorización.
Implementamos la lista usando los arrays dinámicos y estructuras que provee D */

import std.stdio, std.bigint;

struct factor_primario {
    BigInt primo;
    BigInt exponente;
}

factor_primario[] factorize(BigInt n)
{
 factor_primario[] factores;
 for (BigInt d=2;d<=n;d++)
 {
    if (n%d==0)
    {
      BigInt e=0;
      do
      {
        e++;
        BigInt m=n/d;
        writeln(n,"=",m,"*",d);
        n=m;
      }
      while (n%d==0);
      factor_primario factor;
      factor.primo=d;
      factor.exponente=e;
      factores ~= factor;
    }
 }
 return factores;
}

/* Esta función toma la factorizaciòn de un entero calculada por la función anterior y 
 la convierte a un formato agradable para mostrar en la pantalla */

string convert_to_pretty_factorization(factor_primario[] lista)
{
 if (lista.length==0) return "1";
 string text="";
 for (uint i=0;i<lista.length;i++)
  {
    if (i>0)
      text ~= "*";
      factor_primario factor=lista[i];
      text ~=toDecimalString(factor.primo);
      text ~="^";
      text ~=toDecimalString(factor.exponente);
  }
 return text;
}

string pretty_factorization(BigInt n)
{
  auto factores = factorize(n);
  return convert_to_pretty_factorization(factores);
}

void main ()
{
  string numero;
  while(true)
   {
     writeln("Ingrese el número que quiere factorizar");
     readf("%s\n", &numero);   
     writeln("La factorización es\n",numero,"=",pretty_factorization(BigInt(numero)));
   }
}