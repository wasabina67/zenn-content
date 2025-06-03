import unittest
import importlib

module = importlib.import_module("scripts.30")
r = module.r


class Test30(unittest.TestCase):
    def test(self):
        numbers = [1, 2, 3, 4, 5, 8, 9, 10, 12, 13]
        expected = ['1~5', '8~10', '12~13']
        self.assertEqual(r(numbers), expected)


if __name__ == "__main__":
    unittest.main()
