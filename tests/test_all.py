import unittest2

from consecutivesum import whilecount
from lookandsay import lookandsay
from nondivisor import solve


class TestConsecSum(unittest2.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.assertEqual(whilecount(103), [[51,52]])


class TestLookAndSay(unittest2.TestCase):
    def setUp(self):
        pass

    def test_negative(self):
        with self.assertRaises(ValueError): lookandsay(-1)

    def test_zero(self):
        with self.assertRaises(ValueError): lookandsay(0)

    def test_simple(self):
        self.assertEqual(lookandsay(10), '13211311123113112211')


class TestNonDivisor(unittest2.TestCase):
    def test_simple(self):
        self.assertEqual(solve([3, 1, 2, 3, 6]), [2, 4, 3, 2, 0])

    def test_small(self):
        self.assertEqual(solve([2, 4]), [1, 0])