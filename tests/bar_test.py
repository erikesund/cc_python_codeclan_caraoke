import unittest
from src.bar import Bar 

class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(100)

    def test_bar_has_till(self):
        self.assertEqual(100, self.bar.till)