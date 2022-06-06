
from msilib.schema import ODBCSourceAttribute


class Persona:

    nombre = "Oscar"
    passw = "hola12345"
    user = "BLISS"
    correo = "oscar.cris@mail.com"


    suma = 1
    resta = 2
    mult = 3
    div = 4

    #def __init__(self,nombre):
     #   self.nombre = nombre
        #self.edad = edad
    
    def insert(self,nombre):
        self.nombre = nombre