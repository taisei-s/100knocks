# coding;utf-8
"""
00. 文字列の逆順

文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

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