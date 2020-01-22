import unittest
from random import randint
from calculusmodule import *


class TestCase7(unittest.TestCase):

    def setUp(self):
        self.a = randint(0, 100)
        self.b = randint(0, 100)

    def test_Multiplication(self):
        self.assertEqual(multiplication(self.a, self.b), self.a * self.b)



