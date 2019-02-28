# coding:utf-8
"""
09. Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import unittest
from parameterized import parameterized
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing09 import shuffle_inside, swing09

class TestSwings(unittest.TestCase):

    @parameterized.expand([
        ('', ''),
        ('abcd', 'abcd')
    ])

    def test_shuffle_inside_1(self, input, expected):
        actual = shuffle_inside(input)

        self.assertEqual(expected, actual)

    def test_shuffle_inside_2(self):
        word = 'abcde'
        new_word = shuffle_inside(word)

        actual = new_word[0] + new_word[-1]
        expected = word[0] + word[-1]

        self.assertEqual(expected, actual)


    def test_swing09(self):
        str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        new_str = swing09(str)

        expected = len(str)
        actual = len(new_str)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()