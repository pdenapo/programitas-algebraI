

/* Programa para factorizar un número en favtores primos 
- Versión en lenguaje D  

   Esta versión utiliza la tabla de primos generada
   por generar_tabla_de_primos.d
 */

/* Esta función factoriza un entero n y devuelve una lista de pares en un array en la forma [d,e] donde
d es un divisor primo de n y e es el exponente correspondiente en su factorización.
Implementamos la lista usando los arrays dinámicos y estructuras que provee D */

/* import tabla_de_primos; */
import std.stdio;
import std.conv;
/* Para cronometrar la factorización */
import std.datetime.stopwatch;

struct factor_primario {
    ulong primo;
    ulong exponente;
}

factor_primario[] factorize(ulong n)
{
 factor_primario[] factores;
 for (ulong d=2;d<=n;d++)
 {
    if (n%d==0)
    {
      ulong e=0;
      do
      {
        e++;
        ulong m=n/d;
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
      text ~=to!string(factor.primo);
      text ~="^";
      text ~=to!string(factor.exponente);
  }
 return text;
}

string pretty_factorization(ulong n)
{
  StopWatch cronometro;
  cronometro.start();
  auto factores = factorize(n);
  cronometro.stop();
  writefln("Tiempo para factorizarlo: %s milisegundos", cronometro.peek.total!"msecs");
  return convert_to_pretty_factorization(factores);
}

void main ()
{
  string entrada;
  ulong numero;
  while(true)
   {
     writeln("Ingrese el número que quiere factorizar");
     readf("%s\n", &entrada);
     try{
      numero=  to!ulong(entrada);
     } catch (std.conv.ConvException exc){
        writeln("Es un número demasiado grande. Ingrese otro.");
        writeln("Máximo=", ulong.max);
        continue;
       } 
     writeln("La factorización es\n",numero,"=",pretty_factorization(numero));
   }
}