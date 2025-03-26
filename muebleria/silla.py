# Importaciones necesarias
from mueble import Mueble

# clases relacionadas con las sillas
class Silla(Mueble):
    def __init__(self, material, precio, num_patas):
        super().__init__(material, precio)
        self.num_patas = num_patas

    def calcular_precio_final(self):
        return self.precio * 1.32

    # polimorfismo
    def __str__(self):
        return super().__str__() + f"""
Numero de patas: {self.num_patas} 
Precio final: $ {self.calcular_precio_final():.2f}"""