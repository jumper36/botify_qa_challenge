import unittest
from random import randint
from calculusmodule import *


class TestCase6(unittest.TestCase):

    def setUp(self):
        self.a = randint(0, 100)
        self.b = randint(0, 100)

    def test01_Division(self):
        self.assertEqual(division(self.a, self.b), self.a / self.b)

    #handling division by zero
    def test02_DivisionByZero(self):
        self.assertRaises(ZeroDivisionError, division, self.a, 0)

    #handling seed
    def test03_Division(self):
        self.assertAlmostEqual(division(1, 3), 0.33333, 5)
