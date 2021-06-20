#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C)
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.6/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import *

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

       # collatz_eval_1 uses memoization optimization
    def test_eval_1(self):
        a = collatz_eval(1, 10)
        self.assertEqual(a, 20)

    def test_eval_2(self):
        a = collatz_eval(100, 200)
        self.assertEqual(a, 125)

    def test_eval_3(self):
        a = collatz_eval(201, 210)
        self.assertEqual(a, 89)

    def test_eval_4(self):
        a = collatz_eval(900, 1000)
        self.assertEqual(a, 174)

    def test_eval_5(self):
        a = collatz_eval(1, 100000)
        self.assertEqual(a, 351)

    def test_eval_6(self):
        a = collatz_eval(10, 1)
        self.assertEqual(a, 20)

    def test_eval_7(self):
        a = collatz_eval(1, 1)
        self.assertEqual(a, 1)

    def test_eval_8(self):
        a = collatz_eval(10, 10)
        self.assertEqual(a, 7)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n10 1\n1 100000")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n10 1 20\n1 100000 351\n")

# ----
# main
# ----


if __name__ == "__main__": #pragma: no cover
    main()

""" #pragma: no cover
$ coverage run --branch TestCollatz.py >  TestCollatz.out 2>&1


$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          12      0      2      0   100%
TestCollatz.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
