from persona import Persona

i=0
while i<3:
    try:
        persona = Persona()
        nombre = input("escribe tu nombre: ")
        i=i+1
        if nombre.isalpha() == True:
            print("tu nombre es: ",nombre)
            if nombre == persona.nombre:
                print("Correcto")
                break
            else:
                print("no es el correcto")
                if i==3:
                    print("INTENTOS AGOTADOS")
                #break
        else:
            print("no acepta numeros")
            if    i==3:
                  print("INTENTOS AGOTADOS")
    except ValueError:
        print("Error")
