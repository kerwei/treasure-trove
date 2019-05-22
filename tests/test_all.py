import unittest
from consecutivesum import whilecount
from lookandsay import lookandsay

class TestConsecSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.assertEqual(whilecount(103), [[51,52]])


class TestLookAndSay(unittest.TestCase):
    def setUp(self):
        pass

    def test_negative(self):
        with self.assertRaises(ValueError): lookandsay(-1)

    def test_zero(self):
        with self.assertRaises(ValueError): lookandsay(0)

    def test_simple(self):
        self.assertEqual(lookandsay(10), '13211311123113112211')