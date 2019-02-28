# coding;utf-8
"""
10．行数のカウント

行数をカウントせよ．確認にはwcコマンドを用いよ．

command:
wc -l hightemp.txt
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing10 import swing10

class TestSwings(unittest.TestCase):

    def test_swing10(self):
        sys.argv.append('../swings/hightemp.txt')
        expected = 24
        actual = swing10()

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()