# coding:utf-8

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing01 import swing01

class TestSwings(unittest.TestCase):

    def test_swing01(self):
        str = u"パタトクカシーー"
        expected = u"パトカー"
        actual = swing01(str)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()