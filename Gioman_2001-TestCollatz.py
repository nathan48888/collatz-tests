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

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    
    def test_read_2(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)
    
    def test_read_3(self):
        s = "1 100000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 100000)


    # ----
    # eval
    # ----
    
    # collatz_eval_1 uses memoization optimization
    def test_eval_1(self):
        a = collatz_eval(1, 10)
        self.assertEqual(a, 20)
        
        b = collatz_eval(10, 1)
        self.assertEqual(b, 20)

    def test_eval_2(self):
        a = collatz_eval(1, 1)
        self.assertEqual(a, 1)

        b = collatz_eval(100, 200)
        self.assertEqual(b, 125)

    def test_eval_3(self):
        a = collatz_eval(201, 210)
        self.assertEqual(a, 89)

        b = collatz_eval(900, 1000)
        self.assertEqual(b, 174)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n10 1")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n10 1 20\n")
    
    def test_solve_2(self):
        r = StringIO("10 1\n10 10\n 500 101\n1 1")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n10 10 7\n500 101 144\n1 1 1\n")

    def test_solve_3(self):
        r = StringIO("1 100000\n340 30100\n1 98746\n9999 9998")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 100000 351\n340 30100 308\n1 98746 351\n9999 9998 92\n")

    

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
