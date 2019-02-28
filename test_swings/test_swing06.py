# coding:utf-8
"""
06. 集合

"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing06 import swing06

class TestSwings(unittest.TestCase):

    def test_swing06(self):
        str1 = "paraparaparadise"
        str2 = 'paragraph'

        expected = [{'pa', 'ar', 'ra', 'ap', 'ad', 'di', 'is', 'se', 'ag', 'gr', 'ph'}, {'pa', 'ar', 'ra', 'ap'}, {'ad', 'di', 'is', 'se'}, True, False]

        actual = swing06(str1, str2)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()