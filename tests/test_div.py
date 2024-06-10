# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import division

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_division(self):
        assert division(6,3) == 2
        assert division(15,3) == 5
        assert division(24,8) == 3
        assert division(9,9) == 1
