import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testSaludarDeveriaDevolverHola(self):

        saludoEsperado = "Hola"

        saludoRecibido = usuario.saludar()

        self.assertEqual(saludoEsperado,saludoRecibido)