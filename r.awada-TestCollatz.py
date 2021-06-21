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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----
	
	# Create dictionary 
    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

        s = "0 13\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  0)
        self.assertEqual(j, 13)

        s = "7 9\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  7)
        self.assertEqual(j, 9)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(20100, 20001)
        self.assertEqual(v, 243)

    def test_eval_5(self):
        v = collatz_eval(40100 , 50036)
        self.assertEqual(v, 314)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

        w = StringIO()
        collatz_print(w, 824, 905, 179)
        self.assertEqual(w.getvalue(), "824 905 179\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

        r = StringIO("65 651\n669 807\n597 779\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "65 651 145\n669 807 171\n597 779 171\n")

        r = StringIO("181 899\n255 307\n368 705\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "181 899 179\n255 307 123\n368 705 171\n")

# ----
# main
# ----


if __name__ == "__main__":
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
