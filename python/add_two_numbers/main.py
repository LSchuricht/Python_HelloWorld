#!/usr/bin/env python
# https://leetcode.com/problems/add-two-numbers/
# test cases soon
import logging

l1 = [2, 4, 3]
l2 = [5, 6, 4]
output = [7, 0, 8]
logging.basicConfig(level=logging.INFO)


def main(l1, l2):
    l1 = get_number(l1)
    l2 = get_number(l2)
    l3 = build_list(l1 + l2)
    l3.reverse()
    return l3


def get_number(l):
    sum = 0
    exponent = 0
    l.reverse()
    for n in l:
        sum += n * 10**exponent
        exponent += 1
    return sum


def build_list(sum):
    l = []
    sum = str(sum)
    for n in sum:
        l.append(n)
    return l


print(main(l1=l1, l2=l2))
print("hi, lorem sit dolor lorem")
