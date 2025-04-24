# "tomar datos"
class Animal:  
    def __init__(self):  
        self.tamaño = ""
        self.edad = ""
        self.raza = ""

    def comer(self):
        mensaje = "El animal se comio una picha"
        return mensaje

    def dormir(self):
        mensaje = "Al animal lo durmieron"
        return mensaje

# *codigo*
objperro1 = Animal()
objgato1 = Animal()
aux = objgato1.comer()
print(aux)  
aux=objperro1.comer()