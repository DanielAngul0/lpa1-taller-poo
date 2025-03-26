# Importando la clase abstracta 'Mueble'
from mueble import Mueble # Obtiene los atributos material, precio y el metodo abstracto

# --- Subclase de Mueble, relacionada con las mesas ---
class Mesa(Mueble):
    def __init__(self, material, precio, ancho, largo):
        super().__init__(material, precio) # Obtiene los atributos del padre
        self.ancho = ancho # Asigna el ancho de la mesa
        self.largo = largo # Asigna el largo de la mesa

    # Metodo abstracto especifico para la clase Mesa
    def calcular_precio_final(self):
        return self.precio * 1.2 # Precio base aumentado un 20%
    
    # Obtiene la informacion de la clase padre 'Mueble', los atributos especificos de la subclase 'Mesa' y el resultado del metodo abstracto y lo convierte en un formato string legible
    def __str__(self):
        return super().__str__() + f"""
Ancho: {self.ancho} cm 
Largo: {self.largo} cm
Precio final: $ {self.calcular_precio_final():.2f}"""