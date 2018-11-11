

/* Programa para factorizar un número en favtores primos para usar con node.js
   Ejemplo: para factorizar 360 ejecùtelo como

 node factorizar.js 200 */

/* Función que devuelve la factorización de un número n, como una lista de pares [d,e]
   donde d representa a cada uno de los factores primos del nùmero n y e es el exponente correspondiente 
   
   Nota: el código podrìa optimizarse mucho. No está pensado para ser eficiente, sino para que sea fàcil
   de entender.
   */

/* Esta variable la usamos para acumular los textos que queremos devolver en pantalla como resultado */

var output_text="";
const  break_char="\n"

function factorize(n){
factors=[];
for (d=2;d<=n;d++)
 {
    if (n%d==0)
    {
      e=0;  
      do
      {
        e++;
        m=n/d;
        output_text += n+"="+m+"*"+d+break_char;
        n=m;
      }
      while (n%d==0);
      new_factor=[d,e];
      factors.push(new_factor);
    };
 };
 return factors;
};

/* Esta funciòn calcula la factorización de un entero, utilizando la anterior, y la convierte a un formato agradable para mostrar en la pantalla */

function pretty_factorization(n)
{
 factors_list= factorize(n);
 if (factors_list.length==0) return "1";
 text="";
 for (i=0;i<factors_list.length;i++)
  {
    if (i>0)
      text += "*";
      factor=factors_list[i];
      text+=factor[0]+"^"+factor[1];
  };
 return text;
}

/* Main Program code */
/* Es posible un manejor más avanzado la linea de comandos usando comander.js 
 https://github.com/tj/commander.js/  pero tratemos de mantener las cosas lo más simples posibles */

 var numero = process.argv[2];
 output_text="Usted introdujo:" + numero+break_char  
 if(isNaN(numero)){
	output_text += numero + " no es un número"+break_char;
   }
  else{
    factorization=pretty_factorization(numero);
    output_text +="La factorización de "+numero+" es "+factorization+break_char; 
   };   
   console.log(output_text);
 