import is_prime
import unittest


class Test_is_prime(unittest.TestCase):

    def test_basic(self):
        self.assertTrue(is_prime.is_prime(3))
        self.assertTrue(is_prime.is_prime(4))