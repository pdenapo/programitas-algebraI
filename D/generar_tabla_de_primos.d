/* Programita para calcular la tabla de los 
números primos */

import std.stdio;

void main()
{
  /* Cuantos números primos queremos obtener */
  const uint cuantos=30;
  ulong[cuantos] tabla_de_primos;
  tabla_de_primos[0]=2;
  uint tope=1;
  ulong n=3;
  while (tope< cuantos)
  {
    /* Para ver si n es primo o no, vamos dividiendo
    por los primos anteriores en la tabla. Usamos
    la variable booleana es_primo para saber si
    encontramos un factor primo o no */

    bool es_primo=true;
    debug writeln("Testeando si ",n," es primo o no");
    for (uint i=0;i<tope;i++)
    {
      if (n%tabla_de_primos[i]==0)
      {
         debug writeln("NO. Encontramos un factor primo ", tabla_de_primos[i]);
         es_primo= false;
         break;
      }
    }
   if (es_primo)
   {
    debug writeln("SI");
    tabla_de_primos[tope]=n;
    tope++;   
   }
   if (n==ulong.max)
    break;
   n++;
  }
  debug writeln("Total:",tope," primos encontrados");
  writeln("/* Este archivo fue automáticamente generado por 
  el programa generar_tabla_de_primos */"); 
  write("const ulong[",tope,"] tabla_de_primos=[");
  for (uint i=0;i<tope;i++)
  {
    if (i>0)
      write(',');
    write(tabla_de_primos[i]);
  }
  writeln("];");
}