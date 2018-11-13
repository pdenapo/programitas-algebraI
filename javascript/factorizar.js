

/* Programa para factorizar un número en favtores primos para usar con node.js
   Ejemplo: para factorizar 360 ejecùtelo como

 node factorizar.js 360 */

/* Función que devuelve la factorización de un número n, como una lista de pares [d,e]
   donde d representa a cada uno de los factores primos del nùmero n y e es el exponente correspondiente 
   
   Nota: el código podrìa optimizarse mucho. No está pensado para ser eficiente, sino para que sea fàcil
   de entender.
   */

/* JavaScript code should be executed in "strict mode" */

"use strict";

/* Esta variable la usamos para acumular los textos que queremos devolver en pantalla como resultado */


var output_text="";

/* Con esta constante establecemos si queremos usar <br> o \n como salto de lìnea */

var  break_char;

function get_break_char()
{
  if (typeof window === 'undefined') {
  /* running under node.js */
    return "\n";
} else {
    return "<br";
}
}

/* Esta función factoriza un entero n y devuelve una lista de pares en un array en la forma [d,e] donde
d es un divisor primo de n y e es el exponente correspondiente en su factorizaciòn */

function factorize(n){
let factors=[];
for (let d=2;d<=n;d++)
 {
    if (n%d==0)
    {
      let e=0;  
      do
      {
        e++;
        let m=n/d;
        output_text += n+"="+m+"*"+d+break_char;
        n=m;
      }
      while (n%d==0);
      let new_factor=[d,e];
      factors.push(new_factor);
    };
 };
 return factors;
};

/* Esta funciòn toma la factorizaciòn de un entero calculada por la función anterior y 
 la convierte a un formato agradable para mostrar en la pantalla */

function convert_to_pretty_factorization(factors_list)
{
 if (factors_list.length==0) return "1";
 let text="";
 for (let i=0;i<factors_list.length;i++)
  {
    if (i>0)
      text += "*";
      let factor=factors_list[i];
      text+=factor[0]+"^"+factor[1];
  };
 return text;
}

function pretty_factorization(n)
{
  let factors_list= factorize(n);
  return convert_to_pretty_factorization(factors_list);
}

/* Main Program code */
/* Es posible un manejor más avanzado la linea de comandos usando comander.js 
 https://github.com/tj/commander.js/  pero tratemos de mantener las cosas lo más simples posibles */

 if (process.argv.length == 3) 
 {
  var numero = process.argv[2];
 }
  else
 {
  console.log('Este programa requiere exactamente un argumento: el nùmero a factorizar.') 
  return 1;
 };
 break_char= get_break_char();
 output_text="Usted introdujo:" + numero+break_char  
 if(isNaN(numero)){
	output_text += numero + " no es un número"+break_char;
   }
  else{
    let factorization=pretty_factorization(numero);
    output_text +="La factorización de "+numero+" es "+factorization+break_char; 
   };   
   console.log(output_text);
   return 0;
