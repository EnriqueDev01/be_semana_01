'''
INGRESAR PERSONAS
Hacer un programa que primero capture cuantas Personas vamos a ingresar, 
luego pedir su nombre, dni y fecha de nacimiento y al final 
mostrarlas en un orden de la mas joven a la mas adulta
'''

cantidad_personas = int(input("Cantidad de Personas: "))

def leerPersonas(cantidad):    
    personas = {}
    fechas = []
    for i in range(0,cantidad):
        nombre = input(f'Nombre Persona {i+1}: ')
        dni = input(f'Dni Persona {i+1}: ')
        nacimiento = input(f'Fecha nacimiento (yyyy/mm/dd) {i+1}: ')
        nacimiento_clave = int(nacimiento.replace("/", ""))
        personas[nacimiento_clave] = {"nombre": nombre, "dni":dni, "fecha_nacimiento":nacimiento}
        fechas.append(nacimiento_clave)       
    return [fechas, personas]

def ordenarPersonas(Personas):
    fechas = Personas[0]
    fechas.sort(reverse=True)
    print("Personas Ordenadas desde Joven a mas Adulta")
    for fecha in fechas:
        persona = Personas[1][fecha]        
        print(f'Fecha Nacimiento: {persona["fecha_nacimiento"]} - DNI: {persona["dni"]} - NOMBRE: {persona["nombre"]}')

personas = leerPersonas(cantidad_personas)
ordenarPersonas(personas)