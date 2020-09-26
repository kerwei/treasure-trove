import unittest

from consecutivesum import whilecount
from distinctslice import distinct_slice
from lookandsay import lookandsay
from maxproduct import maxproduct
from nondivisor import solve
from minabssum import components


class TestConsecSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(whilecount(103), [[51,52]])

class TestLookAndSay(unittest.TestCase):
    def test_negative(self):
        with self.assertRaises(ValueError): lookandsay(-1)

    def test_zero(self):
        with self.assertRaises(ValueError): lookandsay(0)

    def test_simple(self):
        self.assertEqual(lookandsay(10), '13211311123113112211')

class TestNonDivisor(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(solve([3, 1, 2, 3, 6]), [2, 4, 3, 2, 0])

    def test_small(self):
        self.assertEqual(solve([2, 4]), [1, 0])

class TestMaxProduct(unittest.TestCase):
    def test_small_even(self):
        self.assertEqual(maxproduct(4), 4)

    def test_small_odd(self):
        self.assertEqual(maxproduct(5), 6)

    def test_even(self):
        self.assertEqual(maxproduct(8), 18)

    def test_odd(self):
        self.assertEqual(maxproduct(9), 27)

class TestDistinctSlice(unittest.TestCase):
    def test_simple(self) -> None:
        A = [3, 4, 5, 5, 2]
        self.assertEqual(distinct_slice(6, A), 9)

    def test_single(self) -> None:
        A = [2, 2, 2, 2, 2]
        self.assertEqual(distinct_slice(2, A), 5)

    def test_pair(self) -> None:
        A = [2, 3]
        self.assertEqual(distinct_slice(3, A), 3)

    def test_alternate(self) -> None:
        A = [2, 3, 2, 3]
        self.assertEqual(distinct_slice(3, A), 7)

class TestMinAbsSum(unittest.TestCase):
    def test_simple(self):
        A = [1, 2, 5, 3, 4, 5, 2]
        self.assertEqual(components(A), 0)