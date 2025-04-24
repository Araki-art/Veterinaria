from Animal import Animal
from Cliente import	Cliente
perro = Animal("pequeño", "2 años", "Labrador")
aux_accion=perro.comer()
print(aux_accion)

perro.imprimir_info()

objSebastian= Cliente()
dato_nombre= objSebastian.get_nombre()
print(dato_nombre)
objSebastian.set_nombre("Sebastian")
print(objSebastian.get_nombre())
