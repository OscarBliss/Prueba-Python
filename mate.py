
# while True:
#     n1 = float(input("pon las horas: "))
#     n2 = float(input("pon el costo: "))
#     res = n1 * n2
#     print("tu pago es :",res)
#     break

from persona import Persona

n1 = float(input("pon un numero: "))
n2 = float(input("pon otro numero: "))
oper = int(input("elige el numero de la operacion:\n 1:Suma\n 2:Resta\n 3:Multiplicacion\n 4:Division: "))


while True:
    opc = Persona()
    if oper == opc.suma:
        res = n1 + n2
        print("El resultado es: ",res)
        break
    if oper == opc.resta:
        res = n1 - n2
        print("El resultado es: ",res)
        break
    if oper == opc.mult:
        res = n1 * n2
        print("El resultado es: ",res)
        break
    if oper == opc.div:
        if n1 == 0 and n2 == 0:
            print("Los digitos ingresados deben ser mayor a 0")
            n1 = float(input("pon un numero: "))
            n2 = float(input("pon otro numero: "))
        else:
            if n1 ==0:
                print ("El Resultado Siempre Sera 0")
                n1 = float(input("pon un numero: "))
            elif n2 > 0:
                res = n1 / n2
                print("El resultado es: ",res)
                break
        
            else:
                print("No se puede dividir entre 0")
                n2 =  float(input("pon otro numero:"))
    