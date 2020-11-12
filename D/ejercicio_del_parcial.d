import std.algorithm.iteration;
import std.range : iota;
import std.stdio;
import std.string;

ulong factorial(ulong n)
{
  ulong r=1;
  for (ulong i=1;i<=n;i++)
   r = r*i;
  return r;
}

void main()
{
 //dchar[] palabra = ['F','I','C','C','I'];
 const dchar[] palabra = ['F','I','B','O','N','A','C','C','I'];   
 ulong cuantas_permutaciones=0;
 ulong cuantas_permutaciones_unicas=0;
 ulong cuantas=0;
 string[] permutaciones_unicas;
 
auto permutaciones = palabra.permutations!();
foreach (p;permutaciones) {
   cuantas_permutaciones++;
   string permutacion_como_string;
   foreach (q;p)
   {
    permutacion_como_string ~= q;
   }
    bool es_unica = true;

   bool tiene_dos_c_seguidas = false;
   for (int i=0;i<permutacion_como_string.length-1;i++)
   {
     if (permutacion_como_string[i]=='C' && permutacion_como_string[i+1]=='C')
     {
        tiene_dos_c_seguidas = true;
        break;
     }
   } 

   foreach(s;permutaciones_unicas)
   {
     if (s==permutacion_como_string)
     {
        es_unica= false;
        break; 
     }
   }

   if (es_unica)
   {
      permutaciones_unicas ~= permutacion_como_string;
      cuantas_permutaciones_unicas++;
      //writeln(cuantas_permutaciones_unicas," ",permutacion_como_string);
   }

   if(es_unica && !tiene_dos_c_seguidas)
   {
     cuantas++; 
   }

}

 writeln("Cuantas permutaciones = ",cuantas_permutaciones);
 
 //writeln("Deberían ser = ",factorial(palabra.length));
 // controlamos que sean la cantidad correcta
 assert(cuantas_permutaciones==factorial(palabra.length));
 writeln("Cuantas permutaciones únicas = ",cuantas_permutaciones_unicas);
 assert(cuantas_permutaciones_unicas==factorial(palabra.length)/(factorial(2)*factorial(2)));
 writeln("Respuesta del ejercicio = ", cuantas);
 assert(cuantas == factorial(9)/(factorial(2)*factorial(2))-factorial(8)/factorial(2));
}

// Respuestas
// Cuantas permutaciones = 362880
// Cuantas permutaciones únicas = 90720
// cuantas = 70560 (respuesta del ejercicio)