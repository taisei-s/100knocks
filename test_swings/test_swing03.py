# coding:utf-8

import unittest
from swing03 import swing03

class TestSwings(unittest.TestCase):

    def test_swing03(self):
        str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        actual = swing03(str)

        self.assertEquals(expected, actual)



if __name__ == "__main__":
    unittest.main()