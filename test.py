import unittest
from calculator import Taxes

class calctest(unittest.TestCase):
    def test_normal_1(self):
        purchase = 1000000
        porcentage = 19

        expected_result = 190000
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))
    
    def test_normal_2(self):
        purchase = 200000
        porcentage = 19

        expected_result = 38000
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))

    def test_normal_3(self):
        purchase = 1500000
        porcentage = 19
        discount = 10

        expected_result = 256500
        result = Taxes.calculate(purchase, porcentage, discount)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_1(self):
        purchase = 500000
        porcentage = 0

        expected_result = 0
        result = Taxes.calculate(purchase, porcentage)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_2(self):
        purchase = 1200
        porcentage = 19
        currency = 'USD'

        expected_result = 1026000
        result = Taxes.calculate(purchase, porcentage, currency=currency)

        self.assertEqual(round(expected_result), round(result))

    def test_extraordinary_3(self):
        purchase = 150000
        porcentage = 19
        plastic_bag = 3

        expected_result = 28695
        result = Taxes.calculate(purchase, porcentage, plastic_bag=plastic_bag)

        self.assertEqual(round(expected_result), round(result))

    

        
if __name__ == '__main__':
    unittest.main()