# Importaciones necesarias
from abc import ABC, abstractmethod

# clases relacionadas con los muebles
class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material
        self.precio = precio

    # metodo abstracto que sera implementado por las subclases
    @abstractmethod
    def calcular_precio_final(self):
        pass

    def __str__(self):
        return f"""---{self.__class__.__name__}---
Mueble con material: {self.material}
con un precio de: {self.precio}"""
