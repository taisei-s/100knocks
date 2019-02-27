# coding:utf-8

import unittest
from parameterized import parameterized
from swing09 import shuffle_inside, swing09

class TestSwings(unittest.TestCase):

    @parameterized.expand([
        ('', ''),
        ('abcd', 'abcd')
    ])

    def test_shuffle_inside_1(self, input, expected):
        actual = shuffle_inside(input)

        self.assertEquals(expected, actual)

    def test_shuffle_inside_2(self):
        word = 'abcde'
        new_word = shuffle_inside(word)

        actual = new_word[0] + new_word[-1]
        expected = word[0] + word[-1]

        self.assertEquals(expected, actual)


    def test_swing09(self):
        str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        new_str = swing09(str)

        expected = len(str)
        actual = len(new_str)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()