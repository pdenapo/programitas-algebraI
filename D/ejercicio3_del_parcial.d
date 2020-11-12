
// https://stackoverflow.com/questions/23994066/check-if-array-contains-element-in-d

import std.stdio;
import std.math:abs;

// Calculamos el máximo común divisor por el algoritmo de Euclides
// Este código funciona bien con int, pero no con ulong
int gcd(int a, int b)
{
    if ((a<0) || (b<0))
        return gcd(abs(a),abs(b));
    if (b==0)
        return a;
    // Calculamos el cociente y el resto en la división de a por b    
    else
    {    
        int q = a /b;
        int r = a - b*q;
        return gcd(b,r);
    }    
}

struct Par
{
  int a,b;
}

void main()
{
    const int limite=1000;
    Par [int] posibles_valores;
    for (int a=1;a<limite;a++)
        for (int b=1; b<limite; b++)
        if (gcd(a,b)==3)
        {
           int d= gcd(11*a-7*b,4*a+3*b);
           writeln("a= ",a," b= ",b, " d= ",d);
           if (!(d in posibles_valores))
            posibles_valores[d]= Par(a,b);
        }
    writeln("Posibles valores = ",  posibles_valores);
}
