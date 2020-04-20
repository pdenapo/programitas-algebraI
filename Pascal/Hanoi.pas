program Torre_de_Hanoi ;
{ Implementa el algoritmo de la torre de Hanoi}

const
 maxdisco = 20; {numero maximo de discos-puede cambiarse}

type
 disco = 1..maxdisco; {los discos se representan por enteros}
 estaca = record
             nro_de_estaca: integer; {1,2 o 3}
             torre: array [1..maxdisco] of disco;
               { lista de numeros que simboliza los discos en esta estaca}
             puntero: 0..maxdisco;
               { cuantos discos hay apilados}
           end;
var
 estaca_1,estaca_2,estaca_3: estaca;
 i,n,j: integer; {variables auxiliares}
 paso:longint; {cuenta los pasos realizados}

procedure tomar_ultimo(var A:estaca;var x:disco);
{ devuelve el ultimo de la estaca A,lo desapila}
begin
 if A.puntero <>0 then  {si no esta vacia}
     begin
        x:= A.torre[A.puntero];  {el puntero apunta al ultimo}
        A.puntero := A.puntero-1; {actualiza puntero}
     end
 else
   { si se llega a este punto,se intento una operacion ilegal}
   begin
    writeln ('Es ilegal tomar el ultimo de una estaca vacia!');
    halt(1); { detiene la ejecucion}
   end;
end;
procedure agregar(var A:estaca;x:disco);
{ apila x en la estaca A}
var
 y:disco;
begin
 if A.puntero<>0 then        {si no esta vacia}
   y := A.torre[A.puntero];
 if (A.puntero=0) or (x<y) then
    begin
      A.puntero:= A.puntero+1;
      A.torre[A.puntero] := x;
     end
 else
    begin
    { Si se llego a este punto se intento una operacion ilegal}
      writeln ('Es ilegal apilar un disco mas grande sobre uno mas chico!');
      halt(2); {detiene la ejecucion}
    end;
end;
procedure mover (var A,B:estaca);
{ mueve el ultimo de la estaca A a la estaca B}
var
 x:disco;
begin
 tomar_ultimo(A,x);
 agregar (B,x);
 paso := paso+1;
 writeln ('Paso ',paso,':Se mueve el disco ',x,' de la estaca ',
 A.nro_de_estaca,' a la estaca ',B.nro_de_estaca);
 { Muestra un mensaje explicando la operacion - Se puede cambiar por una
 representacion grafica }
end;
procedure Hanoi (var A,B,C:estaca;n:integer);
{ este algoritmo mueve n discos de la estaca A a la estaca C y a la salida
no modifica la B}
begin
 if n=1 then
   mover (A,C)
 else
  begin
    Hanoi (A,C,B,n-1);   {Esta es la llamada recursiva}
    mover (A,C);
    Hanoi (B,A,C,n-1);   {Esta es otra llamada recursiva}
  end;
end;
begin
 writeln ('Algoritmo de la torre de Hanoi');
 writeln ('Ingrese el numero de discos:');
 readln(n);
 paso :=0;
 estaca_1.nro_de_estaca:=1;
 estaca_2.nro_de_estaca:=2;
 estaca_3.nro_de_estaca:=3;
 { Inicialmente la estaca 1 contine los discos 1 a n}
 estaca_1.puntero :=n;
 i:=1;
 for j:= n downto 1 do
  begin
   estaca_1.torre[j] := i;
   i:=i+1;
  end;
 estaca_2.puntero:=0;
 estaca_3.puntero:=0;
 Hanoi (estaca_1,estaca_2,estaca_3,n);
 writeln ('Listo!');
end.


