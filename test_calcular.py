import unittest
from calcular import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(6, 2), 3)
        self.assertEqual(dividir(-6, 2), -3)
        self.assertEqual(dividir(6, -2), -3)
        self.assertEqual(dividir(-6, -2), 3)
        
        with self.assertRaises(ValueError):
            dividir(6, 0)

if __name__ == '__main__':
    unittest.main()
