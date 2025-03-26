# Importando framework de testeo
import pytest

# Importando datos de todas las clases para realizar los tests
from muebleria.mueble import Mueble
from muebleria.silla import Silla
from muebleria.mesa import Mesa
from muebleria.armario import Armario


# ---- Tests para la clase abstracta Mueble ----

# **** Test para verificar que no pueda instanciarse una clase abstracta ****
def test_clase_abstracta_no_instanciable():
    with pytest.raises(TypeError):
        mueble = Mueble("metal", 200)


# ---- Tests para la subclase Silla ----

# **** Test para verificar que el metodo abstracto se opere correctamente ****
def test_silla_calcular_precio_final():
    silla = Silla("Cuero sintetico", 411621, 4) # Evaluando material, precio, numero de patas
    assert silla.calcular_precio_final() == 543339.72  # 411621 * 1.32
    
# **** Test para verificar que no se reciba un numero de patas incoherente ****
def test_silla_num_patas_invalido():
    with pytest.raises(ValueError):
        Silla("Cuero sintetico", 411621, 0)
    
    
# ---- Tests para la subclase Mesa ----

# **** Test para verificar que no deje efectuar un precio negativo ****
def test_mesa_precio_negativo():
    """Caso de borde: precio negativo (debe lanzar excepción)."""
    with pytest.raises(ValueError):
        Mesa("Madera", -500, 46, 101)

# **** Test para verificar que el programa es capaz de funcionar incluso cuando el material esta vacio ****
def test_mesa_con_material_vacio():
    mesa = Mesa("", 508057, 46, 101) # Evaluando material, precio, ancho, largo
    assert mesa.material == "" # Asignacion de espacio vacio a 'material'
    assert mesa.calcular_precio_final() == 609668.4


# ---- Tests para la subclase Armario ----

# **** Test para verificar que __str__ muestre correctamente los datos del armario ****
def test_armario_str_representation():
    armario = Armario("MDP", 749900, 3)       
        
