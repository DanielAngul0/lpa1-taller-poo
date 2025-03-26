# Importando clases abstractas para crear metodos abstractos
from abc import ABC, abstractmethod

# --- Clase abstracta (Base) ---
class Mueble(ABC):
    def __init__(self, material, precio):
        self.material = material # Asigna el material del mueble
        self.precio = precio # Asigna el precio base del mueble
        self.descuento = 0 # Descuento incial es 0

    # Metodo abstracto que sera implementado por las subclases
    @abstractmethod
    # Este metodo abstracto calculara el precio base para dar como resultado un precio final
    def calcular_precio_final(self):
        pass
    
    # Este metodo aplicara un descuento al precio base segun sea el contexto
    def aplicar_descuento(self, porcentaje):
        
        # Verificando que el porcentaje este entre el rango de 0 a 100
        if not 0 <= porcentaje <= 100: 
            raise ValueError("El descuento debe estar entre 0% y 100%")
        self.descuento = porcentaje

    # Muestra el nombre de la clase del objeto seguido de sus atributos principales en un formato string legible
    def __str__(self):
        return f"""---> {self.__class__.__name__} <---
Material del mueble: {self.material}
Precio: $ {self.precio}"""
