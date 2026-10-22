"""
EJERCICIO 3:
Un curso recibe notas entre 0 y 100, 
una a una, hasta recibir -99.
Muestre la cantidad de notas y su promedio.
El centinela no es una nota y no participa en el
cálculo. 
Si aparece primero, muestre cantidad cero y 
«Sin notas» en lugar de un promedio. 
El flujo siempre contiene -99. 
El promedio es la
suma de las notas aceptadas dividida entre su 
cantidad.
"""
Suma = 0
nota = 0
cantidad = 0
nota = int(input("Digite nota: "))

if nota != -99:
        while 0 <= nota <= 100:
             Suma += nota
             nota = int(input("Digite nota: "))
             cantidad += 1

             if nota == -99:
                  break
        promedio = Suma / cantidad    
        print ("cantidad: ", cantidad)
        print ("promedio: ", promedio)
 
else:
    print ("cantidad de notas: 0 ")
    print ("Sin notas")
    
    
              



    




