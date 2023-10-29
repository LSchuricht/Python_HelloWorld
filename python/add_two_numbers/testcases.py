import main
from unittest import TestCase


class test_basic(TestCase):
    def test_case_1(self):
        mycase = main.add_two_numbers([2, 4, 3], [5, 6, 4])
        mycase.foo()
        self.assertEqual(mycase.l3, ["7", "0", "8"])

    def test_case_2(self):
        mycase = main.add_two_numbers([0, 0], [0])
        mycase.foo()
        self.assertEqual(mycase.l3, ["0"])

    def test_case_3(self):
        mycase = main.add_two_numbers([9, 9], [3])
        mycase.foo()
        self.assertEqual(mycase.l3, ["2", "0", "1"])

    def test_case_4(self):
        mycase = main.add_two_numbers([], [3])
        mycase.foo()
        self.assertEqual(mycase.l3, ["3"])

    def test_case_5(self):
        mycase = main.add_two_numbers([4], [])
        mycase.foo()
        self.assertEqual(mycase.l3, ["4"])

    def test_case_6(self):
        mycase = main.add_two_numbers([], [])
        mycase.foo()
        self.assertEqual(mycase.l3, ["0"])
