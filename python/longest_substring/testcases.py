from main import longest_substring as foo
from unittest import TestCase


class test_basic(TestCase):
    def test_case_1(self):
        s = "abcab"
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 3)

    def test_case_2(self):
        s = "abcabcd"
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 4)

    def test_case_3(self):
        s = "bbbb"
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 1)

    def test_case_4(self):
        s = "Hannah"
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 3)

    def test_case_5(self):
        s = ""
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 0)

    def test_case_6(self):
        s = "abcabcdadcabcdefabc"
        mycase = foo()
        mycase.set(s)
        mycase.find_substring()
        self.assertEqual(mycase.len_longest_substring, 6)
