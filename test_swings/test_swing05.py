# coding:utf-8
"""
05. n-gram

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing05 import swing05

class TestSwings(unittest.TestCase):

    def test_swing05(self):
        str = "I am an NLPer"

        expected = ([['I', 'am'], ['am', 'an'], ['an', 'NLPer']], ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er'])

        actual1, actual2 = swing05(str)
        actual = (actual1, actual2)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()