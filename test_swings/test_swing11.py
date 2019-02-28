# coding;utf-8
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
        expected = "高知県 江川崎 41 2013-08-12\n埼玉県 熊谷 40.9 2007-08-16\n岐阜県 多治見 40.9 2007-08-16\n山形県 山形 40.8 1933-07-25\n山梨県 甲府 40.7 2013-08-10\n和歌山県 かつらぎ 40.6 1994-08-08\n静岡県 天竜 40.6 1994-08-04\n山梨県 勝沼 40.5 2013-08-10\n埼玉県 越谷 40.4 2007-08-16\n群馬県 館林 40.3 2007-08-16\n群馬県 上里見 40.3 1998-07-04\n愛知県 愛西 40.3 1994-08-05\n千葉県 牛久 40.2 2004-07-20\n静岡県 佐久間 40.2 2001-07-24\n愛媛県 宇和島 40.2 1927-07-22\n山形県 酒田 40.1 1978-08-03\n岐阜県 美濃 40 2007-08-16\n群馬県 前橋 40 2001-07-24\n千葉県 茂原 39.9 2013-08-11\n埼玉県 鳩山 39.9 1997-07-05\n大阪府 豊中 39.9 1994-08-08\n山梨県 大月 39.9 1990-07-19\n山形県 鶴岡 39.9 1978-08-03\n愛知県 名古屋 39.9 1942-08-02\n\n"
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()