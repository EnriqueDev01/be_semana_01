''' 
BIENVENIDA
Para este reto tendremos que hacer lo siguiente:
1) Ingresar un nombre y su edad.
2) Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) debe ir a dormir y si no hacer la tarea.
3) Si es mayor de edad que indique que no esta obligado a hacer nada.
'''
import datetime as dt

def bienvenida(nombre, edad):
    hora = dt.datetime.now().hour

    if edad >= 18:
        print(f'{nombre} tienes libertad de hacer lo que gustes')
    else:
        if hora < 18:
            print(f'{nombre} debes hacer la tarea')
        else:
            print(f'{nombre} debes ir a dormir')

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

bienvenida(nombre, edad)

