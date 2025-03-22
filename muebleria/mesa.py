# Importaciones necesarias
from mueble import Mueble

# clases relacionadas con las mesas
class Mesa(Mueble):
    def __init__(self, material, precio, ancho, largo):
        super().__init__(material, precio)
        self.ancho = ancho
        self.largo = largo

    def calcular_precio_final():
        pass
    
    # polimorfismo
    def __str__(self):
        return super().__str__() + f"\nancho {self.ancho} largo {self.largo}"