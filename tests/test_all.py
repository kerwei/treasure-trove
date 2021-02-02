import unittest

from consecutivesum import whilecount
from distinctslice import distinct_slice
from lookandsay import lookandsay
from maxconsecsum import maxconsecsum
from maxproduct import maxproduct
from minabssum import components
from nondivisor import solve
from passwordcombo import password


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

class TestMaxConsecSum(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_simple_one(self) -> None:
        A = [1, -2, 0, 9, -1, -2]
        self.assertEqual(maxconsecsum(A), 8)

    def test_simple_two(self) -> None:
        A = [-1, -2, 0, 9, -1, -2]
        self.assertEqual(maxconsecsum(A), 6)

    def test_negative_one(self) -> None:
        A = [-1, -2, -1, -1, -2, -1, -9, -2]
        self.assertEqual(maxconsecsum(A), -4)

    def test_negative_two(self) -> None:
        # A = [-2] * 8
        A = [-1, -3, -3, -4, -5, -6, -7, -1, -1]
        self.assertEqual(maxconsecsum(A), -5)


class TestPasswordCombo(unittest.TestCase):
    """
    Return all possible combinations of a password from list. Where two or
    more element words are combined, they are concatenated by an underscore
    """
    def test_simple_one(self):
        A = ['one', 'list', 'A', 'of', 'random', 'words', 'four']
        self.assertListEqual(password(A, 6), [
            'A_of_A',
            'of_A_A',
            'A_A_of',
            'random',
            'of_one',
            'one_of',
            'list_A',
            'four_A',
            'A_list',
            'A_four'
        ])