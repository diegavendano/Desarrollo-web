#!/usr/bin/python3

# guardar como 'ejemplo_funciones.py'
# en la carpeta del proyecto.

# las funciones en python parten con def...
#esta es una funcion muy sencilla

def funcion_tonta(nombre):
    separador = " "
    print(separador.join(("Hola", nombre, "eres Tonto/a")))

#Llamamos a la funcon directamente...
funcion_tonta("diego")

#
#
def digito_verificador(rut_sin_digito):
    digito = ""
    multiplo = 0
    acumulador = 0
    contador = 2
    while rut_sin_digito > 0:
        multiplo = (rut_sin_digito % 10) * contador
        acumulador = acumulador + multiplo
        rut_sin_digito = rut_sin_digito // 10 # Division Entera
        contador = contador + 1
        if contador == 8:
            contador = 2
    digito = 11 - (acumulador % 11)
    if digito == 10:
        digito = 'K'
    if digito == 10:
        digito = 0
    return digito

mi_rut = 20207507
print("-".join((str(mi_rut), str(digito_verificador(mi_rut)))))

