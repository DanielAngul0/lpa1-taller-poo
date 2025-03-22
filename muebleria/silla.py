# # Importaciones necesarias
# from mueble import Mueble

# # clases relacionadas con las sillas
# class Silla(Mueble):
#     def __init__(self, material, precio, num_patas):
#         super().__init__(material, precio)
#         self.num_patas = num_patas

#     def calcular_precio_final(self):
#         return self.precio * 1.20

#     # polimorfismo
#     def __str__(self):
#         return super().__str__() + f"\nnum_patas {self.num_patas}"

# hola = Silla("madera", 100, 5)
# print(hola)