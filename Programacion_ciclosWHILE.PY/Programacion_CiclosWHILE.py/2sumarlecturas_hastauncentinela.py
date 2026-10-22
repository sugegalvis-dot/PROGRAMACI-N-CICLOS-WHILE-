""" 
Ejercicio 2
Una actividad recibe números uno a uno hasta que aparezca -50.
MUestre la suma de toda las lecturas anteriores
-50 no forma parte de los datos y nunca se suma 
Los demás valores incluidos negativos distintos de -50
y el cero, si participan.
Si el primer dato es -50, la suma es cero. 
El flujo siempre contiene la centinela.
"""

suma = 0 



while True:
    num = int(input("Digite un numero: "))
    if num != -50:
        suma += num
    else:
        break
print ("Suma: ", suma)


