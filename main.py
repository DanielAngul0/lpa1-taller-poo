# Importaciones de las subclases para los objetos
from muebleria.silla import Silla # Importa material, precio y numero de patas de la clase Silla
from muebleria.mesa import Mesa # Importa material, precio y dimensiones de la clase Mesa
from muebleria.armario import Armario # Importa material, precio y numero de puertas de la clase Armario

# Creando objetos de cada clase
# Datos representados: Material, precio y caracteristica propia de cada mueble
silla = Silla("Cuero sintetico", 411621, 4) # 4 patas
mesa = Mesa("Madera", 508057, 46, 101) # 46x101 cm
armario = Armario("MDP", 749900, 3) # 3 puertas

# Descuentos
silla.aplicar_descuento(15)
mesa.aplicar_descuento(25)
armario.aplicar_descuento(7)

# Imprime datos de los objetos en cadena de texto
# print(silla)
# print(mesa)
# print(armario)

# Imprime datos de los objetos en una tabla estetica
silla.mostrar_info_rich()
mesa.mostrar_info_rich()
armario.mostrar_info_rich()
