#!/usr/bin/env python3

# -------------
# Exceptions.py
# -------------

# https://docs.python.org/3.8/library/exceptions.html

def f(b):
    if b:
        raise NameError("abc")
    return 0

print("Exceptions.py")

try:
    assert f(False) == 0
except NameError:
    assert False

expected_args = ("abc",)  

try:
    assert f(True) == 1
    assert False
except NameError as e:
    assert isinstance(e, NameError)
    assert isinstance(e.args, tuple)
    assert len(e.args) == 1
    assert e.args is not expected_args  
    assert e.args == expected_args
else:
    assert False

assert isinstance(NameError, type)
assert isinstance(type,      type)

assert issubclass(NameError,     Exception)
assert issubclass(Exception,     BaseException)
assert issubclass(NameError,     BaseException)
assert issubclass(BaseException, object)

print("Done.")
