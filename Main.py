from Animal import Animal
from Cliente import	Cliente
perro = Animal("pequeño", "2 años", "Labrador")
aux_accion=perro.comer()
print(aux_accion)

perro.imprimir_info()

objPolla= Cliente()
dato_nombre= objPolla.get_nombre()
print(dato_nombre)
objPolla.set_nombre("Polla")
print(objPolla.get_nombre())
