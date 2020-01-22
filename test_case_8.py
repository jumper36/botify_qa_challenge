import unittest
from random import randint
from calculusmodule import *


class TestCase8(unittest.TestCase):

    def setUp(self):
        self.a = randint(0, 100)
        self.b = randint(0, 100)

    def test_Percentage(self):
        self.assertEqual(percentage(self.a, self.b), (self.a / self.b) * 100)



