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

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    
    def test_read_2(self):
        s = "0 5\n"
        with self.assertRaises(AssertionError):
            collatz_read(s)

    def test_read_3(self):
        s = "22 12\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 12)
        self.assertEqual(j, 22)

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
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        with self.assertRaises(AssertionError):
            v = collatz_eval(-2, 36)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 15, 27, 112)
        self.assertEqual(w.getvalue(), "15 27 112\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 89, 900, 179)
        self.assertEqual(w.getvalue(), "89 900 179\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("2 8\n46 91\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "2 8 17\n46 91 116\n")

    def test_solve_3(self):
        r = StringIO("47 96\n899 1264\n1496 1702\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "47 96 116\n899 1264 182\n1496 1702 180\n")

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
