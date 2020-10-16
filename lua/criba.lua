--- ... representa un parámetro que podemos pasarle
--- en este caso hasta donde queremos calcular la tabla de primos
local n = ... or 1000
local criba = {}
local primos = {}

--- incialemnte ningún número fue tachado en la criba
for i = 2, n do criba[i] = true end

for i = 2, n do
 if criba[i] then
   -- encontramos un primo, lo agregamos a la lista
   primos[#primos+1] = i
   -- tachamos sus múltiplos, son compuestos
   print("tachamos los múltiplos de ", i)
   for j = i*2, n, i do criba[j] = false end
 end
end

for i = 2, n do 
  print(i,criba[i])
end

-- Muestra la lista de primos    

print(table.concat(primos, " "))
