
/* Implementación de la función phi de Euler en C 
  (diferentes métodos para comparar)

Calcula el máximo común divisor de dos números a y b, y los coeficientes 
que permiten escribirlo como una combinación lineal de ambos.

Este programa tiene solamente propósitos didácticos (es para mis alumnos
de Algebra I).

Ha sido desarrollado sobre el sistema GNU/Linux pero debería funcionar
sobre cualquier sistema compatible con el standard POSIX, dado que 
sólo utiliza llamnadas a la librería C estándar.

(C) 2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

Este programa es software libre, y usted puede redistribuirlo o 
modificarlo libremente bajo los términos de la 
GNU General Public Licence (Licencia Pública General), versión 2
o cualquier versión posterior, 
publicada por la Free Software Foundation. Vea:

http://www.gnu.org/copyleft/gpl.html

*/


#include <stdio.h>

int gcd (int x,int y)
/* calcula el maximo comun divisor por el algoritmo de Euclides */
{
if (y == 0) 
  return(x);
else
  return(gcd(y,x % y));
};

int phi (int x)
/* calcula el valor de la funcion phi de Euler */
/* algoritmo muy ingenuo ... */
{
int i;
int s; 
s = 1;
for (i=2; i < x ; i++) 
 if (gcd(x,i)==1) s++;
return(s);
};

int phi2 (int x)
/* un algoritmo mejor : usa factorizacion */
{
int d;
int y;
if (x==1) return(1);
for (d=2; d*d <= x; d++)
/* solo es necesario dividir hasta la raiz cuadrada de x */
{
  if (x % d == 0)
  {
  
/* Si se llego a este punto, d es el primer divisor de x , que necesariamente
es primo. Calculamos en y el valor d^(c-1) donde c es el mayor exponente tal
que d^c divide a x y en x queda x / d^c . d^c e x/d^c son coprimos. Y por
otro lado phi(d^c)= (d-1)*d^c. Ahora usamos la propiedad multiplicativa */     
     
     x = x / d;
     y = 1;
     while (x%d == 0)
       {   
         x = x /d ;
         y = y * d ;
       };
    return ((d-1)*y*phi2(x));   
   }
 }
 /* si se llega a este punto , x es primo */
 return (x-1);
};



int phi3 (int x)
/* un algoritmo mejor : usa factorizacion -version no recursiva */
{
int d;
int z;
if (x==1) return(1);
/* z acumula los resultados parciales , que se van multiplicando */
z=1;
for (d=2; d*d <= x; d++)
/* solo es necesario dividir hasta la raiz cuadrada de x */
{
  if (x % d == 0)
  {

/* Si se llego a este punto, d es el primer divisor de x , que necesariamente
es primo. Multiplicamos z por el valor phi(d^c)= (d-1)*d^(c-1) donde c es el 
mayor  exponente tal que d^c divide a x y en x queda x / d^c . 
d^c e x/d^c son  coprimos y usamos la propiedad multiplicativa */     
     
     x = x / d;
     z = z * (d-1);
     while (x%d == 0)
       {   
         x = x /d ;
/* como x no es divisible por 2,3,...,d-1 , x/d tampoco */         
         z = z * d ;
       };   
   }
 }
 /* cuando se llega a este punto , x=1 o x  es primo 
 (pues x no es divisible por ningun numero menor que su raiz
 cuadrada */
 if (x!=1) z = z * (x-1);
 return(z);
};



void main(void)
{
 int i;
 printf("Calculo de la funcion phi de euler\n");
 do
 {
   printf("Ingrese un numero:");
   scanf("%i",&i);
   printf("metodo 1 = %i \n",phi(i)); 
   printf("metodo 2 = %i \n",phi2(i));
   printf("metodo 3 = %i \n",phi3(i));
} while (i!=1);
};