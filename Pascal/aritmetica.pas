unit aritmetica;
{Unit que implementa diversas funciones aritméticas

(C) 2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

Este programa es software libre, y usted puede redistribuirlo o 
modificarlo libremente bajo los términos de la 
GNU General Public Licence (Licencia Pública General), versión 2
o cualquier versión posterior, 
publicada por la Free Software Foundation. Vea:

http://www.gnu.org/copyleft/gpl.html

}
interface
function indicador(x:integer):integer;
function mcd (x,y:integer):integer;
function mcm (x,y: integer):integer;
function coprimos (x,y:integer):boolean;
function Ramanujan (x,n: integer):integer;
function Mobius(x:integer):integer;
function primo (x:integer):boolean;
implementation
{funciones aritmeticas}
function mcd (x,y:integer):integer;
{calcula el maximo comun divisor por el algoritmo de Euclides}
begin
if y = 0 then mcd := x else mcd:= mcd(y,x mod y);
end;
function mcm (x,y: integer):integer;
{calcula el minimo comun multiplo}
begin
mcm := x*y div mcd (x,y);
end;
function coprimos (x,y:integer):boolean;
{determina si son primos entre si}
begin
coprimos := mcd (x,y) =1;
end;
function indicador (x:integer):integer;
{calcula el valor del indicador de Euler}
var
i,s: integer;
begin
s:= 0;
for i:= 1 to x do
if coprimos (x,i) then inc(s);
indicador := s;
end;
function Ramanujan (x,n: integer):integer;
{calcula la suma de Ramanujan}
var
s,k,i:integer;
begin
k := mcd (x,n);
s:= 0;
for i:= 1 to k do
if k mod i = 0 then s:= s + mobius(x div i)* i;
ramanujan := s;
end; {de Ramanujan}
function Mobius(x:integer):integer;
{funcion de mobius}
var
i:integer;
begin
if x = 1 then
 mobius :=1
else
 begin
  i:= 2;
  while (i< x) and (x mod i <> 0) do
  inc (i);
  if x mod sqr(i) = 0 then
   mobius := 0
  else
   mobius := - mobius (x div i);
 end;
end ; {de Mobius}
function primo (x:integer):boolean;
{determina si x es primo}
var
i:integer;
r: boolean;
begin
if x = 1 then
 primo := false
else
 begin
  r:= true;
  for i := 2 to x-1 do
  r:= r and (x mod i <> 0) ;
  primo := r;
 end;
end; {de primo}
end.