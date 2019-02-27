# coding;utf-8

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing00 import swing00

class TestSwings(unittest.TestCase):

    def test_swing00(self):
        str = "stressed"
        expected = "desserts"
        actual = swing00(str)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()