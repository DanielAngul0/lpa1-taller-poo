# Importaciones necesarias
from mueble import Mueble

# clases relacionadas con los armarios
class Armario(Mueble):
    def __init__(self, material, precio, num_puertas):
        super().__init__(material, precio)
        self.num_puertas = num_puertas

    # polimorfismo
    def __str__(self):
        return super().__str__() + f"\nnum_puertas {self.num_puertas}"