# Cargamos el módulo unittest
import unittest
import sys
import os.path
sys.path.insert(0, r'C:\Users\Carlota Martin-Anero\OneDrive\Documentos\UAX\Tercero de carrera GMAT\5º cuatri\Desarrollo orientado a objetos\calcu\calculadora-tdd-01-empezamos\carpeta')

from Calculator import *
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
# Creamos una prueba para probar un valor inicial
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_suma (self):
        # Ejecutamos el método
        self.calc.suma(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

    def test_resta(self):
        # Ejecutamos el método
        self.calc.resta(4, 2)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    def test_division(self):
        # Ejecutamos el método
        self.calc.división(4, 2)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(2, self.calc.value)

    def test_mult(self):
        # Ejecutamos el método
        self.calc.producto(3, 2)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(6, self.calc.value)

    def test_factorial(self):
        # Ejecutamos el método
        self.calc.factorial(4)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(24, self.calc.value)

    def test_potencia(self):
        # Ejecutamos el método
        self.calc.potencia(3, 4)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(81, self.calc.value)

if __name__ == '__main__':
    unittest.main()

