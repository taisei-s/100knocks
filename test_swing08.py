# coding:utf-8

import unittest
from parameterized import parameterized
from swing08 import swing08

class TestSwings(unittest.TestCase):

    @parameterized.expand([
        ('abcd', ['zyxw', 'abcd']),
        ('ABCD', ['ABCD', 'ABCD']),
        (u'あいうえ', [u'あいうえ', u'あいうえ']),
        ('1234', ['1234', '1234']),
        ('(){%}|\\', ['(){%}|\\', '(){%}|\\']),
        ('Hello, Python World.', ['Hvool, Pbgslm Wliow.', 'Hello, Python World.'])
    ])

    def test_swing08(self, input, expected):
        actual1, actual2 = swing08(input)
        actual = [actual1, actual2]
        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()