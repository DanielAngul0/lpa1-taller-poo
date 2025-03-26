# Importando clases abstractas para crear metodos abstractos
from abc import ABC, abstractmethod

# --- Clase abstracta (Base) ---
class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material # Asigna el material del mueble
        self.precio = precio # Asigna el precio base del mueble

    # Metodo abstracto que sera implementado por las subclases
    @abstractmethod
    def calcular_precio_final(self):
        pass

    # Muestra el nombre de la clase del objeto seguido de sus atributos principales en un formato string legible
    def __str__(self):
        return f"""---> {self.__class__.__name__} <---
Material del mueble: {self.material}
Precio: $ {self.precio}"""
