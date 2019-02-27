# coding:utf-8

import unittest
from swing05 import swing05

class TestSwings(unittest.TestCase):

    def test_swing05(self):
        str = "I am an NLPer"

        expected = ([['I', 'am'], ['am', 'an'], ['an', 'NLPer']], ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er'])

        actual1, actual2 = swing05(str)
        actual = (actual1, actual2)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()