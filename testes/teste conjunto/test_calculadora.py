import unittest
import calc

class testeCalc(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calc.soma(10,10), 20)


    def test_subtrair(self):
        self.assertEqual(calc.subtrair(10,10), 0)
        


if __name__ == '__main__':
    unittest.main()