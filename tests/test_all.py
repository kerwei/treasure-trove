import unittest
from consecutivesum import whilecount

class TestConsecSum(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        self.answer = [[51,52]]
        self.assertEqual(whilecount(103), self.answer)