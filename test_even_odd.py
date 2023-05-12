import unittest
from even_odd import even_odd


class TestEvenOdd(unittest.TestCase):

    def test_even(self):
        self.assertEqual(even_odd(2), "Even")
        self.assertEqual(even_odd(4), "Even")
        self.assertEqual(even_odd(100), "Even")


if __name__ == '__main__':
    unittest.main()
