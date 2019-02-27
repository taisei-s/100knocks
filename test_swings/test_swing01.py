# coding:utf-8

import unittest
from swing01 import swing01

class TestSwings(unittest.TestCase):

    def test_swing01(self):
        str = u"パタトクカシーー"
        expected = u"パトカー"
        actual = swing01(str)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()