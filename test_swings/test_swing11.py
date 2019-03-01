# coding:utf-8
"""
11. タブをスペースに置換

タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

commnad:
$sed -e s/'\t'/' '/g hightemp.txt
$cat hightemp.txt | tr '\t' ' '
$expand -t 1 hightemp.txt
"""

from io import StringIO
import unittest
from unittest.mock import patch
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing11 import swing11

class TestSwings(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_swing11(self, mock_stdout):
        sys.argv.append('../swings/hightemp.txt')
        swing11()
        actual = mock_stdout.getvalue()

        self.assertFalse('\t' in actual)
        self.assertTrue(' ' in actual)



if __name__ == "__main__":
    unittest.main()