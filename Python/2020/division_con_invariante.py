def division(a,b): 
    print("division(",a,",",b,")")
    if a<b:
        nuevo_q =0
        nuevo_r =a
    else:
        nuevo_a=a-b
        print(a,"-",b,"=",nuevo_a)
        q,r= division(nuevo_a,b)
        nuevo_q = q+1
        nuevo_r = r
        print("Invariante:",a,"=",b,"*",nuevo_q,
        "+",nuevo_r)
    invariante= (a==b*nuevo_q+nuevo_r)
    if not(invariante):
        print("Error")
    return (nuevo_q,nuevo_r)
   
division(17,3)