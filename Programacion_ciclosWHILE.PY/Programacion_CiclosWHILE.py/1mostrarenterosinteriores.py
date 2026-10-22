"""
EJERCICIO 1

Recibe dos enteros A y B 
A < B. Muestre en orden Ascendente todos
los enteros estrictamente mayores que A
y menores que B.

Los extremos no se muestran. Si no hay enteros
entre ellos informe: <<No hay enteros interiore>>"""

A = int(input("Ingrese entero A: "))
B = int(input("Ingrese entero B (mayor que A): "))

while A < B:
    for i in range (A+1, B):
        print (i)
    break


while A+1 == B:
    print ("No hay enteros interiores")
    break
