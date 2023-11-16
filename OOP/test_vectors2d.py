import unittest
from oop10_spec_methods import Vector2d


class TestVector2d(unittest.TestCase):
    def setUp(self):
        self.v0 = Vector2d.zero()
        self.v1 = Vector2d(1, 2)
        self.v2 = Vector2d(10, 5)

    def test1(self):
        '''Test str(), repr()'''
        self.assertEqual('<x=1.000, y=2.000>', str(self.v1))
        self.assertEqual('<x=10.000, y=5.000>', repr(self.v2))

    def test2(self):
        '''Test add()'''
        self.assertEqual(Vector2d(11, 7), self.v1 + self.v2)
        self.assertEqual(Vector2d(11, 7), self.v2 + self.v1)
        self.assertEqual(self.v2, self.v2 + self.v0)
        self.assertEqual(self.v2, self.v0 + self.v2)
        self.assertEqual(self.v0, self.v0 + self.v0)
        self.assertEqual(self.v2, self.v2 + 0)
        self.assertEqual(Vector2d(1, 1), self.v0 + 1)
        self.assertEqual(Vector2d(1, 1), 1 + self.v0)
        self.assertEqual(Vector2d(20, 15), 10 + self.v2)

        with self.assertRaises(TypeError):
            self.v1 + str(10)

    def test3(self):
        '''Test sub()'''
        self.assertEqual(Vector2d(-9, -3), self.v1 - self.v2)
        self.assertEqual(Vector2d(9, 3), self.v2 - self.v1)
        self.assertEqual(self.v2, self.v2 - self.v0)
        self.assertEqual(Vector2d(-10, -5), self.v0 - self.v2)
        self.assertEqual(self.v0, self.v0 + self.v0)

    def test4(self):
        '''Test mul()'''
        self.assertEqual(20, self.v1 * self.v2)
        self.assertEqual(20, self.v2 * self.v1)
        self.assertEqual(0, self.v2 * self.v0)
        self.assertEqual(0, self.v0 * self.v2)
        self.assertEqual(0, self.v0 * self.v0)
        self.assertEqual(self.v2, self.v2 * 1)
        self.assertEqual(Vector2d(50, 25), self.v2 * 5)
        self.assertEqual(Vector2d(50, 25), 5 * self.v2)
        self.assertEqual(Vector2d(20, 15), 10 + self.v2)

    def test5(self):
        '''Test sorting'''
        vectors = sorted([self.v1, self.v2, self.v0])
        self.assertEqual(self.v0, vectors[0])
        self.assertEqual(self.v1, vectors[1])
        self.assertEqual(self.v2, vectors[2])
        self.assertTrue(vectors[0] < vectors[1])
        self.assertTrue(vectors[1] < vectors[2])



if __name__ == '__main__':
    unittest.main(verbosity=2)

