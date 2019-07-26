import unittest
import primes

class tester(unittest.TestCase):
    def runTest(self):
        self.assertEqual(primes.between_primes(1,10), [2,3,5,7])
        self.assertEqual(primes.between_primes(5,5) , [])
        self.assertEqual(primes.between_primes(257,347), [257,263,269,271,277,281,283,293,307,311,313,317,331,337])
        

        self.assertRaises(ValueError, primes.between_primes('3','6'))
        self.assertRaises(ValueError, primes.between_primes('', ''))
        self.assertRaises(ValueError, primes.between_primes('3', 5))
        self.assertRaises(ValueError, primes.between_primes(5, '3'))
        self.assertRaises(ValueError, primes.between_primes('e', 6))

        self.assertRaises(primes.RangeError, primes.between_primes(10,5))



if __name__ == '__main__':
    unittest.main()
