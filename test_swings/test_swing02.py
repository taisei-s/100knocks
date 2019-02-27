# coding:utf-8

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing02 import swing02

class TestSwings(unittest.TestCase):

    def test_swing02(self):
        str1 = u"パトカー"
        str2 = u"タクシー"
        expected = u"パタトクカシーー"
        actual = swing02(str1, str2)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()