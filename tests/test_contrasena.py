import unittest
from generador_contrasenas.contrasena import GeneradorContrasena

class TestGeneradorContrasena(unittest.TestCase):
    def test_generar_contrasena(self):
        generador = GeneradorContrasena()
        contrasena = generador.generar_contrasena(4, 2, 2, 10)
        self.assertEqual(len(contrasena), 10)

    def test_generar_contrasena_longitud(self):
        generador = GeneradorContrasena()
        contrasena = generador.generar_contrasena(4, 2, 2, 12)
        self.assertEqual(len(contrasena), 12)

if __name__ == '__main__':
    unittest.main()
