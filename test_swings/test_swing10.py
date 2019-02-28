# coding;utf-8
"""
10．行数のカウント

行数をカウントせよ．確認にはwcコマンドを用いよ．

command:
wc -l hightemp.txt
"""

from io import StringIO
import unittest
from unittest.mock import patch
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing10 import swing10

class TestSwings(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_swing10(self, mock_stdout):
        sys.argv.append('../swings/hightemp.txt')
        swing10()
        expected = '24\n'
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()