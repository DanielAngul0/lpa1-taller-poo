# Importando la clase abstracta 'Mueble'
from mueble import Mueble # Obtiene los atributos material, precio y el metodo abstracto

# --- Subclase de Mueble, relacionada con los armarios ---
class Armario(Mueble):
    def __init__(self, material, precio, num_puertas):
        super().__init__(material, precio) # Obtiene los atributos del padre
        self.num_puertas = num_puertas # Asigna el numero de puertas del armario

    # Metodo abstracto especifico para la clase Armario
    def calcular_precio_final(self):
        return self.precio * 1.1 # Precio base aumentado un 10%
    
    # Obtiene la informacion de la clase padre 'Mueble', los atributos especificos de la subclase 'Armario' y el resultado del metodo abstracto y lo convierte en un formato string legible
    def __str__(self):
        return super().__str__() + f"""
Numero de puertas: {self.num_puertas}
Precio final: $ {self.calcular_precio_final():.2f}"""