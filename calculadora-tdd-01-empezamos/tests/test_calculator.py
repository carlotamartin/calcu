# Cargamos el módulo unittest
import unittest
import sys
import os.path
sys.path.insert(0, r'C:\Users\Carlota Martin-Anero\OneDrive\Documentos\UAX\Tercero de carrera GMAT\5º cuatri\Desarrollo orientado a objetos\calcu\calculadora-tdd-01-empezamos\carpeta')
from prueba.Calculator import Calculator
# Creamos una clase heredando de TestCase
class TestMyCalculator(unittest.TestCase):
# Creamos una prueba para probar un valor inicial
    def setUp(self):
        self.calc = Calculator()

    def test_initial_value(self):
        self.assertEqual(0, self.calc.value)

    # Creamos un nuevo test para comprobar una suma
    def test_add_method(self):
        # Ejecutamos el método
        self.calc.suma(1, 3)
        # Comprobamos si el valor es el que esperamos
        self.assertEqual(4, self.calc.value)

