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
        s = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "200 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 200)
        self.assertEqual(j, 100)  

    def test_read_3(self):
        s = "3 50\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  3)
        self.assertEqual(j, 50)

    def test_read_4(self):
        s = "15000 15000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  15000)
        self.assertEqual(j, 15000)

    def test_read_5(self):
        s = "12345 4567\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  12345)
        self.assertEqual(j, 4567)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 900)
        self.assertEqual(v, 55)

    def test_eval_5(self):
        v = collatz_eval(12345, 4567)
        self.assertEqual(v, 268)

    def test_eval_6(self):
        v = collatz_eval(15000, 15000)
        self.assertEqual(v, 178)


    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 50, 3, 112)
        self.assertEqual(w.getvalue(), "50 3 112\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 500, 500, 111)
        self.assertEqual(w.getvalue(), "500 500 111\n")
    
    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n210 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n210 210 40\n900 1000 174\n")

    def test_solve_2(self):
        r = StringIO("50 3\n100 500\n6 83\n40 96\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "50 3 112\n100 500 144\n6 83 116\n40 96 116\n")

    def test_solve_3(self):
        r = StringIO("67 920\n291 503\n32 124\n90 843\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "67 920 179\n291 503 144\n32 124 119\n90 843 171\n")

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
