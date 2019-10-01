#!/usr/bin/python3

#Guardar en la carpeta del proyrcto como:
#'Persona.py'

class Persona:
    """Clase que representa a una persona en Chile
        self -> rol similar al this de Java
        el constructor se llama siempre
        (doble underscore)init(doble underscore)
        Todas las operaciones de la clase reciben
        al self como primer parametro!!!
    """

    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
    
    #OJO todos los metodos reciben el self como parametro!
    def imprimir(self):
        texto = " ".join(["soy", self.nombre, ", mi rut es",self.rut ])
        print(texto)

