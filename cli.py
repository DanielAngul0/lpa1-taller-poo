import argparse # Maneja codigo de lineas de comando
import json # Importacion de serializacion y deserializacion
from muebleria.inventario import Inventario # Importando clase especializada en el control de inventario
# Importando atributos principales y heredados
from muebleria.silla import Silla # Importa material, precio y numero de patas de la clase Silla 
from muebleria.mesa import Mesa # Importa material, precio y dimensiones de la clase Mesa
from muebleria.armario import Armario # Importa material, precio y numero de puertas de la clase Armario

# Mostrara todo el inventario existente de los muebles por consola
def mostrar_inventario(inventario):
    print("\nInventario:")
    if not inventario.muebles:
        print("El inventario esta vacio")
    for mueble in inventario.muebles:
        print(mueble)
        print("-" * 40)

# Creara un mueble segun las caracteristicas proporcionadas
def crear_mueble(args):
    if args.agregar == "Silla":
        return Silla(args.material, args.precio, args.num_patas)
    elif args.agregar == "Mesa":
        return Mesa(args.material, args.precio, args.ancho, args.largo)
    elif args.agregar == "Armario":
        return Armario(args.material, args.precio, args.num_puertas)
    else:
        raise ValueError("Tipo de mueble no reconocido: " + args.agregar)
    
# Aplicara un descuento segun sea su tipo
def aplicar_descuento(inventario, tipo, descuento):
    for mueble in inventario.muebles:
        if isinstance(mueble, tipo):
            mueble.aplicar_descuento(descuento)
            print(f"Descuento de {descuento}% aplicado a {mueble.__class__.__name__}.")
            break

# Serializa el inventario a formato JSON
def serializar_inventario(inventario):
    json_str = inventario.serializar()
    print("\nInventario serializado:")
    print(json_str)

# Deserializa un inventario desde JSON
def deserializar_inventario(inventario, json_str):
    nuevo_inventario = Inventario.deserializar(json_str)
    print("\nInventario deserializado:")
    mostrar_inventario(nuevo_inventario)

def main():
    inventario = Inventario() # Se crea una instancia del objeto inventario para acceder a el
    inventario.cargar_desde_json() # Cargar el inventario desde el archivo JSON

    # Configuración del parser de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Sistema de gestión de inventario de muebles")
    parser.add_argument("--ver", action="store_true", help="Ver el inventario")
    parser.add_argument("--agregar", type=str, choices=["Silla", "Mesa", "Armario"], help="Agregar un mueble")
    parser.add_argument("--material", type=str, help="Material del mueble")
    parser.add_argument("--precio", type=float, help="Precio del mueble")
    parser.add_argument("--num_patas", type=int, help="Número de patas (solo para Silla)")
    parser.add_argument("--ancho", type=int, help="Ancho (solo para Mesa)")
    parser.add_argument("--largo", type=int, help="Largo (solo para Mesa)")
    parser.add_argument("--num_puertas", type=int, help="Número de puertas (solo para Armario)")
    parser.add_argument("--descuento", type=int, help="Aplicar descuento en %")
    parser.add_argument("--serializar", action="store_true", help="Serializar el inventario")
    parser.add_argument("--deserializar", type=str, help="Deserializar el inventario desde JSON")
    parser.add_argument("--debug", action="store_true", help="Mostrar el estado interno del inventario.")
    
    # El 'args' aliza los argumentos pasados por línea de comandos (como --agregar Silla --material Madera), los valida según la configuración del ArgumentParser, y los convierte en un objeto fácil de usar en el código.
    args = parser.parse_args() 

    # Operando con 'args'
    # Mostrar inventario existente de muebles
    if args.ver:
        mostrar_inventario(inventario)

    # Agregar nuevo mueble por linea de comando
    if args.agregar:
        nuevo_mueble = crear_mueble(args)  # ✅ Utilizamos 'args' después de su definición
        inventario.agregar_mueble(nuevo_mueble)  # Cambié 'agregar' por 'agregar_mueble'
        print(f"{args.agregar} agregado exitosamente.")
        print("Inventario actual:", [m.to_dict() for m in inventario.muebles])
        
        # Guardar el inventario actualizado en un archivo aparte 'inventario.json'
        with open('inventario.json', 'w') as f:
            f.write(inventario.serializar())

    # Se aplicara el descuento sobre el mueble seleccionado
    if args.descuento is not None:
        if args.agregar is None:
            print("Debes especificar el tipo de mueble para aplicar el descuento.")
        else:
            if args.agregar == "Silla":
                aplicar_descuento(inventario, Silla, args.descuento)
            elif args.agregar == "Mesa":
                aplicar_descuento(inventario, Mesa, args.descuento)
            elif args.agregar == "Armario":
                aplicar_descuento(inventario, Armario, args.descuento)

    # Sección para serializar el inventario a JSON
    if args.serializar:
        serializar_inventario(inventario)

    # Modo de depuración (debug)
    if args.debug:
        print("Estado del inventario:", [m.to_dict() for m in inventario.muebles])

# Verifica que el codigo se ejecute en el archivo 'main' principal
if __name__ == "__main__":
    main()
