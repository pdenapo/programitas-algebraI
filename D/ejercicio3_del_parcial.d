
// https://stackoverflow.com/questions/23994066/check-if-array-contains-element-in-d

import std.stdio;
import std.numeric:gcd;
import std.algorithm: canFind;
import std.algorithm.sorting;

void main()
{
    const ulong limite=1000;
    ulong[] posibles_valores;
    for (ulong a=1;a<limite;a++)
        for (ulong b=1; b<limite; b++)
        if (gcd(a,b)==3)
        {
           ulong d= gcd(11*a-7*b,4*a+3*b);
           writeln("a= ",a," b= ",b, " d= ",d);
           if (!posibles_valores.canFind(d))
            posibles_valores ~= d;
        }
    posibles_valores.sort();
    writeln("Posibles valores = ",  posibles_valores);
}
