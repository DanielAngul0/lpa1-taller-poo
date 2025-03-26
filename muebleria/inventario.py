import json # Importamos JSON para trabajar en su formato

# Clase para gestionar el inventario de la mueblería
class Inventario:
    def __init__(self):
        # Se crea una lista vacia en la que se guardara cada subclase de 'Mueble' como silla, mesa, armario
        # Esta lista se actualizara cada vez que se agregue un nuevo mueble
        self.muebles = [] 

    def agregar_mueble(self, mueble):
        # Tomara las instancias de objetos de las subclases de 'Mueble' y las añadira a la lista usando el metodo 'append'
        self.muebles.append(mueble)

    def eliminar_mueble(self, mueble):
        # Eliminara unicamente un mueble existente en el inventario, para poder quitar un objeto mueble
        if mueble in self.muebles:
            self.muebles.remove(mueble)
        else:
            print("El mueble no se encuentra en el inventario.")

    def mostrar_inventario(self):
        # Presentara todos los muebles existentes en el inventario
        if not self.muebles:
            print("El inventario está vacío.")
        else:
            for mueble in self.muebles:
                print(mueble)
                print("-" * 40)
                
    # Este método convierte una lista de objetos 'mueble' en una cadena JSON            
    def serializar(self):
        muebles_list = [mueble.to_dict() for mueble in self.muebles] # Recorre cada objeto en la lista 'muebles' y llama al método 'to_dict()' de cada uno, este metodo convierte cada objeto en un diccionario
        return json.dumps(muebles_list, indent=4) # Convierte la lista del diccionario en un formato JSON
    
    # Este método es el opuesto de serializar: convierte una cadena JSON en una instancia de la clase Inventario con los muebles cargados desde el JSON            
    @staticmethod
    def deserializar(json_str):
        #Deserializa la cadena JSON y devuelve una instancia de Inventario con los muebles cargados
        import importlib

        # Convierte la cadena JSON 'json_st' de nuevo en una lista de diccionarios. Cada diccionario representa un mueble con sus atributos.
        muebles_list = json.loads(json_str)
        inventario = Inventario()
        for mueble_data in muebles_list:
            tipo = mueble_data.get("tipo")
            modulo = importlib.import_module(f"muebleria.{tipo.lower()}")
            clase = getattr(modulo, tipo) # Obtiene la clase del modulo segun su tipo de mueble
            mueble = clase.from_dict(mueble_data) # Este método reconstruye el objeto mueble a partir del diccionario mueble_data.
            inventario.agregar_mueble(mueble)
        return inventario
