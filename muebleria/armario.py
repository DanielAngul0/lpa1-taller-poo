# Importaciones necesarias
from mueble import Mueble

# clases relacionadas con los armarios
class Armario(Mueble):
    def __init__(self, material, precio, num_puertas):
        super().__init__(material, precio)
        self.num_puertas = num_puertas

    def calcular_precio_final(self):
        return self.precio * 1.1
    
    # polimorfismo
    def __str__(self):
        return super().__str__() + f"""
Numero de puertas: {self.num_puertas}
Precio final: $ {self.calcular_precio_final():.2f}"""