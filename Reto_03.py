'''
PRODUCTOS POO
Tener un programa que reciba una cantidad de productos a ingresar, que luego de ingresarlos (instanciar) 
podamos llamar a uno de ellos y que nos muestre su descripción y si no, 
tengamos una opción para terminar el programa. (Usar if elif else y while)
'''
cantidad_productos = int(input("Cantidad de Productos: "))

class Producto:
    def __init__(self, nombre, descripcion) -> None:
        self.nombre = nombre
        self.descripcion = descripcion

def programa(cantidad):
    productos = []
    
    for i in range(0,cantidad):
        nombre = input(f'Nombre Producto {i+1}: ')
        descripcion = input(f'Descripcion {i+1}: ')
        productos.append(Producto(nombre,descripcion))
    
    continuar = True
    while continuar:        
        producto = input("NOMBRE PRODUCTO PARA BUSCAR: ")
        descripcion = [(x.descripcion) for x in productos if x.nombre==producto]
        if  len(descripcion)>0:
            print("DESCRIPCION:", descripcion[0])
        else:
            print("No Existe Producto")            
        opcion = input("Desea Terminar el Programa [S=salir]: ")
        if opcion.upper() == "S":
            continuar = False            
            

programa(cantidad_productos)
