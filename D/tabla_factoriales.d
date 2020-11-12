import std.stdio;

ulong factorial(ulong n)
{
  ulong r=1;
  for (ulong i=1;i<n;i++)
   r = r*i;
  return r;
}

void main()
{
   for (ulong n=0;n<20; n++)
      writeln("factorial(",n,")=",factorial(n));
}

