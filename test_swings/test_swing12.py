# coding:utf-8
"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存

各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

import unittest
from unittest import mock
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing12 import swing12, write_file

class TestSwings(unittest.TestCase):

    def test_write_file(self):
        mockio = mock.mock_open()
        with mock.patch("swing12.open", mockio):
            write_file('test.txt', 'test')

        mockio.assert_called_once_with('test.txt', 'w')
        handle = mockio()
        handle.write.assert_called_once_with('test')

    @mock.patch('swing12.write_file')
    def test_swing12(self, mock_write_file):
        sys.argv.append('../swings/hightemp.txt')
        swing12()
        mock_write_file.assert_any_call('col1.txt', "高知県\t江川崎\t41\t2013-08-12\n")
        mock_write_file.assert_any_call('col2.txt', "埼玉県\t熊谷\t40.9\t2007-08-16\n")



if __name__ == "__main__":
    unittest.main()