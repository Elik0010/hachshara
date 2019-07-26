from math import factorial
import unittest


class Tester(unittest.TestCase):
    def runTest(self):
        print("starting tests")
        self.assertEqual(factorial(6), 720, "they should be equal")
        self.assertEqual(factorial(1), 1, "1! is 1")
        self.assertEqual(factorial(0), 1, "They should be equal")
        with self.assertRaises(ValueError):
            factorial(-111)
            factorial(2.5)
            factorial('e')
        print("finishing tests")


unittest.main()
