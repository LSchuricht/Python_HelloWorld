#!/usr/bin/env python
# https://leetcode.com/problems/add-two-numbers/
# test cases soon
import logging

# from unittest import TestCase

logging.basicConfig(level=logging.INFO)


l1 = [2, 4, 3]
l2 = [5, 6, 4]
output = [7, 0, 8]


class add_two_numbers:
    def __init__(self, l1, l2) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = None

    def foo(self):
        self.l1 = add_two_numbers.get_number(self.l1)
        self.l2 = add_two_numbers.get_number(self.l2)
        self.l3 = add_two_numbers.build_list(self)
        self.l3.reverse()
        return self.l3

    def get_number(l):
        l.reverse()
        sum = 0
        exponent = 0
        for n in l:
            sum += n * 10**exponent
            exponent += 1
        return sum

    def build_list(self):
        l = []
        sum = str(self.l1 + self.l2)
        for n in sum:
            l.append(n)
        return l

    def print_list(self):
        return self.l3


sum = add_two_numbers([2, 4, 3], [5, 6, 4])
sum.foo()
print(sum.print_list())
