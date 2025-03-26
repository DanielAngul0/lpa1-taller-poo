# Importando la clase abstracta 'Mueble'
from mueble import Mueble # Obtiene los atributos material, precio y el metodo abstracto

# --- Subclase de Mueble, relacionada con las sillas ---
class Silla(Mueble):
    def __init__(self, material, precio, num_patas):
        super().__init__(material, precio) # Obtiene los atributos del padre
        self.num_patas = num_patas # Asigna el numero de patas de la silla

    # Metodo abstracto especifico para la clase Silla
    def calcular_precio_final(self):
        return self.precio * 1.32 # Precio base aumentado un 32%

    # Obtiene la informacion de la clase padre 'Mueble', los atributos especificos de la subclase 'Silla' y el resultado del metodo abstracto y lo convierte en un formato string legible
    def __str__(self):
        return super().__str__() + f"""
Numero de patas: {self.num_patas} 
Precio final: $ {self.calcular_precio_final():.2f}"""