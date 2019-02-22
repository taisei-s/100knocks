# coding;utf-8

import unittest
from swing00 import swing00

class TestSwings(unittest.TestCase):

    def test_swing00(self):
        str = "stressed"
        expected = "desserts"
        actual = swing00(str)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()