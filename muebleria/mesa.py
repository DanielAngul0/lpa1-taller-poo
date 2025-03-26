# Importando la clase abstracta 'Mueble'
from muebleria.mueble import Mueble # Obtiene los atributos material, precio y el metodo abstracto

# Importando la libreria 'Rich'
from rich.console import Console # Encargado de imprimir en la consola en un formato enriquecido   
from rich.table import Table # Permite crear tablas con bordes y colores

# --- Subclase de Mueble, relacionada con las mesas ---
class Mesa(Mueble):
    def __init__(self, material, precio, ancho, largo):
        
        # Validación de precio positivo
        if precio <= 0:
            raise ValueError("El precio debe ser un valor positivo")
        
        super().__init__(material, precio) # Obtiene los atributos del padre
        self.ancho = ancho # Asigna el ancho de la mesa
        self.largo = largo # Asigna el largo de la mesa

    # Metodo abstracto especifico para la clase Mesa
    def calcular_precio_base(self):
        return self.precio * 1.2 # Precio base aumentado un 20%
    
    # Obtiene la informacion de la clase padre 'Mueble', los atributos especificos de la subclase 'Mesa' y el resultado del metodo abstracto y lo convierte en un formato string legible
    def __str__(self):
        return super().__str__() + f"""
Ancho: {self.ancho} cm 
Largo: {self.largo} cm
Precio final: $ {self.calcular_precio_final():.2f}"""

    # Funcion para crear una tabla estetica de Rich para mostrarla en consola
    def mostrar_info_rich(self):
        consola = Console() # Renderizado inicial de la tabla

        # Creando titulo para la clase 'Mesa' y columnas de la tabla con estetica
        tabla = Table(title="Informacion de la Mesa", style='white')
        tabla.add_column("Atributo", style='#FF0000')
        tabla.add_column("Valor", style='#7F1313')

        # Creando filas de la tabla y añadiendo atributos especificos y metodos abstractos en formato string
        tabla.add_row("Material:", self.material)
        tabla.add_row("Precio base:", f"$ {self.precio}")
        tabla.add_row("Descuento aplicado:", f"{self.descuento}%")
        tabla.add_row("Ancho:", str(self.ancho) + " cm")
        tabla.add_row("Largo:", str(self.largo) + " cm")
        tabla.add_row("Precio final:", f"$ {self.calcular_precio_final():.2f}")

        # Renderizado final de la tabla
        consola.print(tabla)
        
    # 'to_dict(self)' Convierte los atributos de la instancia de un objeto en un diccionario, para representar el objeto de una manera mas simple
    def to_dict(self):
        return {
            "tipo": "Mesa", # Identificador del tipo de mueble para la deserialización
            "material": self.material,
            "precio": self.precio,
            "descuento": self.descuento,
            "ancho": self.ancho,
            "largo": self.largo
        }
        
    # Método de clase para crear una instancia desde un diccionario
    # El diccionario (data) contiene los datos necesarios para reconstruir el objeto
    @classmethod
    def from_dict(cls, data):
        instancia = cls(data["material"], data["precio"], data["ancho"], data["largo"])
        
        # Se aplicara el descuento si existe en los datos
        if "descuento" in data:
            instancia.aplicar_descuento(data["descuento"])
        
        return instancia
        
        
            