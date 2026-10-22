"""
Ejercicio 4:
Una nómina ficticia recibe primero el salario
 mensual de un trabajador. Cero termina el 
registro y no requiere otros datos. 
Un salario mensual positivo se acompaña de días 
trabajados, entero de 0 a 30,bonos no negativos 
y otras deducciones no negativas. 
Muestre el pago neto de cada trabajador, en
orden de lectura. 
La retención es 5 % y el aporte de seguridad 
es 12 % del devengado. Se garantiza que
las otras deducciones no superan el devengado 
después de esos descuentos."""

salario=0
bonos = 0
deducciones=0

salario = int(input("Digite el salario mensual: "))
salario = salario

while salario == 0:
    print ("Sin trabajadores")
    break

while salario > 0:
    dias = int(input("Digite dias trabajados: "))
    bonos = int(input("Digite los bonos: "))
    deducciones = int(input("Digite otras deducciones: "))
    
    if 0<= dias <= 30 and bonos > 0 and deducciones >0:
        salario=salario
        proporcional = salario * dias / 30
        devengado = proporcional + bonos
        Neto = devengado * 0.83 - deducciones
    print ("Neto: ",Neto)
    break
