import unittest
from ejemplo1Pruebas import area
from math import pi

class TestArea(unittest.TestCase):
    def test_area(self):
        print('------Test valores de resultado conocido---')
        self.assertAlmostEqual(area(-1), pi)
        #Hemos probado con un resultado -1 que sabemos que no es posible (ver apuntes tema 7)
        self.assertAlmostEqual(area(0), -1)
        self.assertAlmostEqual(area(3), pi*(3**2))

        print('------Test valores negativos---')
        #Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, -1)

    def test_tipos(self):
        print('Test de tipos no compatibles')
        # Test de tipos no compatibles.
        # Verificamos si el tipo de los parámetros es el correcto.
        # El tipo de la excepción debe ser TypeError
        # Hacemos una prueba para que cada tipo conocido no válido
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, "dos")
        self.assertRaises(TypeError, area, 2+3j)
