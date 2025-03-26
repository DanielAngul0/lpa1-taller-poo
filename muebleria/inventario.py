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
