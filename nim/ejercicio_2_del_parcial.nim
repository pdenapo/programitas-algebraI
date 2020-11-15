import itertools

when isMainModule:
    import itertools
    import strutils # to join seq[char] into a string
    let word="FIBONACCI"
    var permutaciones_diferentes =0
    var cuantas=0 
    for p in distinctPermutations(word):
        inc(permutaciones_diferentes)
        var contiene_dos_c_seguidas = false
        for i in countup(0,p.len-2):
            if p[i]=='C' and p[i+1]=='C':
                 contiene_dos_c_seguidas = true
                 break
        if not(contiene_dos_c_seguidas):
            inc(cuantas)
        echo p.join
    echo "permutaciones diferentes=",permutaciones_diferentes
    # permutaciones diferentes = 90720
    echo "respuesta del ejercicio=",cuantas



