program ciclotom;
{ calcula los polinomios ciclotomicos 
(C) 2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

Este programa es software libre, y usted puede redistribuirlo o 
modificarlo libremente bajo los términos de la 
GNU General Public Licence (Licencia Pública General), versión 2
o cualquier versión posterior, 
publicada por la Free Software Foundation. Vea:

http://www.gnu.org/copyleft/gpl.html
}

uses aritmetica,polien;
var
polinomio: poli_en;
grado : exp_poli_en;
n ,i,j,s: integer;
tecla : char;
begin
 tecla := '1';
 while tecla <> 'x' do
 begin
  write ('n= ?');
  readln (n);
  grado := indicador (n);
  poli_nulo (polinomio);
  polinomio [grado] := 1;
  for i:= 1 to grado do
   begin
   s:= 0;
   for j:= 0 to i-1 do
    s:= s + polinomio [grado-j]*Ramanujan(n,i-j);
   polinomio [grado-i] := - s div i;
  end;
 writeln_poli_en (polinomio);
end;
end.
