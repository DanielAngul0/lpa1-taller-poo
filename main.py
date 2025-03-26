# Importaciones de las subclases para los objetos
from muebleria.silla import Silla # Importa material, precio y numero de patas de la clase Silla
from muebleria.mesa import Mesa # Importa material, precio y dimensiones de la clase Mesa
from muebleria.armario import Armario # Importa material, precio y numero de puertas de la clase Armario
from muebleria.inventario import Inventario

# Creando objetos de cada clase
# Datos representados: Material, precio y caracteristica propia de cada mueble
silla = Silla("Cuero sintetico", 411621, 4) # 4 patas
mesa = Mesa("Madera", 508057, 46, 101) # 46x101 cm
armario = Armario("MDP", 749900, 3) # 3 puertas

# Descuentos
silla.aplicar_descuento(15)
mesa.aplicar_descuento(25)
armario.aplicar_descuento(7)

# --- Gestión del Inventario ---

# # Se crea una instancia del objeto inventario para usar sus metodos y manejar la lista de muebles
inventario = Inventario() 

# Agregar los muebles al inventario
# Se llama al metodo 'agregar_mueble()' para añadir silla, mesa y armario al inventario
inventario.agregar_mueble(silla)
inventario.agregar_mueble(mesa)
inventario.agregar_mueble(armario)

# Serializar el inventario a JSON
# Este método convierte el inventario y todos los 'muebles' dentro de él en una cadena JSON.
json_str = inventario.serializar()
print("Inventario serializado:")
print(json_str)

# Deserializar el JSON para reconstruir el inventario
# Este método recibe la cadena JSON json_str y la convierte de nuevo en una instancia de la clase Inventario, cargando los muebles desde los datos contenidos en el JSON.
nuevo_inventario = Inventario.deserializar(json_str)
print("\nInventario deserializado:")
nuevo_inventario.mostrar_inventario()

# # Mostrara el inventario existente
# print("Inventario de muebles:")
# inventario.mostrar_inventario() # llamara al metodo 'mostrar_inventario()' de 'inventario.py' para traer todos los muebles almacenados

# Imprime datos de los objetos en cadena de texto
# print(silla)
# print(mesa)
# print(armario)

# Imprime datos de los objetos en una tabla estetica
# silla.mostrar_info_rich()
# mesa.mostrar_info_rich()
# armario.mostrar_info_rich()