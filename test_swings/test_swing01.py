# coding:utf-8
"""
01. 「パタトクカシーー」

「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing01 import swing01

class TestSwings(unittest.TestCase):

    def test_swing01(self):
        str = u"パタトクカシーー"
        expected = u"パトカー"
        actual = swing01(str)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()