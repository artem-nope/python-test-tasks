import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    def setUp(self):
        self.f0 = Fraction(0, 5)
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(10, 5)
        self.f3 = Fraction(1, 4)

    def test1(self):
        '''Test str(), repr()'''
        self.assertEqual('The fraction: <numerator=1, denominator=2', str(self.f1))
        self.assertEqual('The fraction: <numerator=10, denominator=5', repr(self.f2))

    def test2(self):
        '''Test add()'''
        self.assertEqual(Fraction(1, 2), self.f1 + self.f0)
        self.assertEqual(Fraction(1, 2), self.f0 + self.f1)
        self.assertEqual(Fraction(3, 4), self.f1 + self.f3)
        self.assertEqual(Fraction(3, 4), self.f3 + self.f1)
        self.assertEqual(self.f1, self.f1 + 0)
        self.assertEqual(self.f1, 0 + self.f1)
        self.assertEqual(Fraction(3, 2), self.f1 + 1)
        self.assertEqual(Fraction(3, 2), 1 + self.f1)
        with self.assertRaises(TypeError):
            self.f1 + str(10)

    def test3(self):
        '''Test sub()'''
        self.assertEqual(Fraction(1, 2), self.f1 - self.f0)
        self.assertEqual(Fraction(-1, 2), self.f0 - self.f1)
        self.assertEqual(Fraction(1, 4), self.f1 - self.f3)
        self.assertEqual(Fraction(-1, 4), self.f3 - self.f1)
        self.assertEqual(self.f1, self.f1 - 0)
        self.assertEqual(Fraction(-1, 2), self.f1 - 1)
        self.assertEqual(Fraction(1, 2), 1 - self.f1)
        with self.assertRaises(TypeError):
            self.f1 - str(10)

    def test4(self):
        '''Test mul()'''
        self.assertEqual(0, self.f0 * self.f1)
        self.assertEqual(0, self.f1 * self.f0)
        self.assertEqual(Fraction(1, 8), self.f1 * self.f3)
        self.assertEqual(Fraction(1, 8), self.f3 * self.f1)
        self.assertEqual(self.f1, self.f1 * 1)
        self.assertEqual(self.f1, 1 * self.f1)
        self.assertEqual(Fraction(5, 2), self.f1 * 5)
        self.assertEqual(Fraction(5, 2), 5 * self.f1)

    def test5(self):
        '''Test dividing'''
        self.assertEqual(0, self.f0 / self.f1)
        self.assertEqual(Fraction(1, 8), self.f1 / 4)
        self.assertEqual(Fraction(8, 1), 4 / self.f1)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(Fraction(1, 8), self.f1 / 0)

    def test6(self):
        '''Test float'''
        self.assertEqual(0.0, float(self.f0))
        self.assertEqual(0.5, float(self.f1))
        self.assertEqual(2.0, float(self.f2))
        self.assertEqual(0.25, float(self.f3))

    def test7(self):
        '''Test int'''
        self.assertEqual(0, int(self.f0))
        self.assertEqual(0, int(self.f1))
        self.assertEqual(2, int(self.f2))
        self.assertEqual(0, int(self.f3))

    def test8(self):
        '''Test bool'''
        self.assertFalse(bool(self.f0))
        self.assertTrue(bool(self.f1))
        self.assertTrue(bool(self.f2))
        self.assertTrue(bool(self.f3))

    def test9(self):
        '''Test sorting'''
        fractions = sorted([self.f1, self.f2, self.f3, self.f0])
        self.assertEqual(self.f0, fractions[0])
        self.assertEqual(self.f3, fractions[1])
        self.assertEqual(self.f1, fractions[2])
        self.assertTrue(fractions[0] < fractions[1])
        self.assertTrue(fractions[1] < fractions[2])


if __name__ == '__main__':
    unittest.main(verbosity=2)

