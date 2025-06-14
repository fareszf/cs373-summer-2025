#!/usr/bin/env python3

#pylint: disable = redefined-variable-type

# ------------
# Operators.py
# ------------

# https://docs.python.org/3.8/library/operator.html

from operator import add

print("Operators.py")

s = "a"
t = "bc"
expected_str = "abc"
u = s + t
assert u is not expected_str
assert u == expected_str

a = (2,)
b = (3, 4)
expected_tuple = (2, 3, 4)
c = a + b
assert c is not expected_tuple
assert c == expected_tuple
assert c != [2, 3, 4]

s = "abc"
t = 2 * s
expected_rep_str = "abcabc"
assert t is not expected_rep_str
assert t == expected_rep_str

a = (2, 3, 4)
expected_rep_tuple = (2, 3, 4, 2, 3, 4)
b = 2 * a
assert b is not expected_rep_tuple
assert b == expected_rep_tuple

print("Done.")
