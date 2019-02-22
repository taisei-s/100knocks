# coding:utf-8

import unittest
from swing07 import swing07

class TestSwings(unittest.TestCase):

    def test_swing07(self):
        x = 12
        y = u"気温"
        z = 22.4

        expected = u"12時の気温は22.4"
        actual = swing07(x, y, z)
        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()