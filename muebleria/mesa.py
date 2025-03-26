# Importaciones necesarias
from mueble import Mueble

# Implementación de la clase Mesa que hereda de Mueble
class Mesa(Mueble):
    def __init__(self, material, precio, ancho, largo):
        super().__init__(material, precio)
        self.ancho = ancho
        self.largo = largo

    def calcular_precio_final(self):
        return self.precio * 1.2
    
    # polimorfismo
    def __str__(self):
        return super().__str__() + f"""
Ancho: {self.ancho} cm 
Largo: {self.largo} cm
Precio final: $ {self.calcular_precio_final():.2f}"""