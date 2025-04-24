class Animal:
    # Metodo constructor
    def __init__(self, dato_tamaño , dato_edad, dato_raza):
        # Atributos
        self.tamaño = dato_tamaño
        self.edad = dato_edad 
        self.raza = dato_raza
        self.estado = "Animal Chillando.."
        print(self.estado)  

    def llorar(self):
        mensaje = "Animal Chillando.."
        return mensaje 

    def comer(self):
        mensaje = "Animal Pichando.."
        return mensaje

    def dormir(self):
        mensaje = "Animal pichado.." 
        return mensaje

    def imprimir_info(self):
        mensaje = "tamaño: " + self.tamaño + ", raza: " + self.raza + ", edad: " + self.edad
        print(mensaje)
    
    