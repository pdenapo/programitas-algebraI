unit polien;
{ operaciones con polinomios enteros 

(C) 2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

Este programa es software libre, y usted puede redistribuirlo o 
modificarlo libremente bajo los términos de la 
GNU General Public Licence (Licencia Pública General), versión 2
o cualquier versión posterior, 
publicada por la Free Software Foundation. Vea:

http://www.gnu.org/copyleft/gpl.html

}
interface
 const

{ constantes modificables }

  max_grad_en = 200 ; {maximo grado de un polinomio entero}

{ constantes no modificables }

  es_nulo = -1 ; {valor devuelto por grado para indicar polinomio nulo}

type
  exp_poli_en = 0..max_grad_en ; {exponente en un polinomio entero}
  poli_en = array [exp_poli_en] of integer; {polinomio entero}

{ procedimientos varios }

  procedure poli_nulo (var p:poli_en);
  function eval_poli_en (p: poli_en;a:integer):integer;
  function evar_poli_en (p: poli_en;a:real):real;
  function grado (p: poli_en) :integer;

{ escribe un polinomio en la pantalla}

  procedure write_poli_en ( p: poli_en);
  procedure writeln_poli_en ( p: poli_en);

{ lee un polinomio,devuelve el grado }

  function read_poli_en ( var p:poli_en):exp_poli_en;

{ operaciones con polinomios }

  procedure suma (var p,q,r : poli_en);
  function Ruffini (p: poli_en;var q:poli_en;a:integer):integer;

implementation
 procedure poli_nulo (var p:poli_en);
 { asigna el polinomio nulo a una variable }
 var
  i: exp_poli_en;
 begin
  for i:= 0 to Max_grad_en do
   p[i]:= 0
  end;
 function eval_poli_en (p: poli_en;a:integer):integer;
 { calcula el valor de p(x) cuando x=a,a entero }
 var
 i: exp_poli_en;
 s : integer;
 begin
 s :=0;
 for i:= max_grad_en downto 0 do
  s:= s*a+p[i];
 eval_poli_en := s
 end;
 function evar_poli_en (p: poli_en;a:real):real;
 { calcula el valor de p(x) cuando x=a,a real }
 var
 i: exp_poli_en;
 s : real;
 begin
 s :=0;
 for i:= max_grad_en downto 0 do
  s:= s*a+p[i];
 evar_poli_en := s
 end;
 function grado (p: poli_en):integer;
 { determina el grado de p(x) }
 { devuelve el valor es_nulo = -1 si es nulo }
 var
 i: exp_poli_en;
 begin
 i := max_grad_en;
 while p[i] = 0 do dec(i);
 grado := i;
 end;
 procedure write_poli_en ( p: poli_en);
 var
  otro_antes :boolean;
  i: exp_poli_en;
 function signo (i:integer):char;
 begin
 if i<0 then
  signo := '-'
 else
  signo := '+'
 end; {de signo}
 begin {de write_poli_en}
  otro_antes := false;
  for i := max_grad_en downto 0 do
   if p[i] =0
    then
   begin
    if (i = 0) and not(otro_antes) then write ('0')
   end
    else
    begin
     if otro_antes or (p[i]<0) then
     write (signo(p[i]));
     otro_antes := true;
     if (abs(p[i])<> 1) or (i=0) then write (abs(p[i]));
     if (abs(p[i])<> 1) and (i<>0) then write ('*');
     if i >1 then write ('x^',i);
     if i =1 then write ('x')
    end;
end; {de write_poli_en}
procedure writeln_poli_en ( p: poli_en);
begin
 write_poli_en (p);
 writeln
end;
function read_poli_en ( var p:poli_en):exp_poli_en;
{ lee un polinomio devuelve el grado }
var
 n,i:exp_poli_en;
begin
 write ('grado = ?');
 readln (n);
 for i:= max_grad_en downto n+1 do
  p[i] := 0;
 for i:= n downto 0 do
  begin
  write ('coeficiente de x^',i,'= ?');
  readln (p[i]);
  end;
 read_poli_en := n;
end;
procedure suma (var p,q,r : poli_en);
{ suma de polinomios p(x) := q (x) + r(x) }
var
 i: exp_poli_en;
begin
 for i:= 0 to max_grad_en do
  p[i] := q[i] + r[i];
end;
function Ruffini (p: poli_en;var q:poli_en;a:integer):integer;
{ divide p(x) por x-a devuelve el resto y almacena el cociente en q(x) }
var
 i: exp_poli_en;
begin
q[max_grad_en] := 0;
for i:= max_grad_en -1 downto 0 do
 q[i] := q[i+1]*a+p[i+1];
Ruffini := q[0]*a+p[0]
end;
end. {de polien }



