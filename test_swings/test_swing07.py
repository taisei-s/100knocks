# coding:utf-8
"""
07. テンプレートによる文生成

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing07 import swing07

class TestSwings(unittest.TestCase):

    def test_swing07(self):
        x = 12
        y = u"気温"
        z = 22.4

        expected = u"12時の気温は22.4"
        actual = swing07(x, y, z)
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()