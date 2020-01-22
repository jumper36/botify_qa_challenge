import unittest
from random import randint
from calculusmodule import *


class TestCase4(unittest.TestCase):

    def setUp(self):
        self.a = randint(0, 100)
        self.b = randint(0, 100)

    def test_Addition(self):
        self.assertEqual(addition(self.a, self.b), self.a + self.b)

