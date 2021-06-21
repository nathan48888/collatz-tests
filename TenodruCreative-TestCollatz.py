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

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    #a normal test
    def test_read_1(self):
        s = "3 33\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  3)
        self.assertEqual(j, 33)

    def test_read_2(self):
        s = "100 250\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 100)
        self.assertEqual(j, 250)

    def test_read_3(self):
        s = "1 900000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 900000)


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
        v = collatz_eval(3, 33)
        self.assertEqual(v, 112)

    def test_eval_6(self):
        v = collatz_eval(100, 250)
        self.assertEqual(v, 128)

    def test_eval_7(self):
        v = collatz_eval(1, 900000)
        self.assertEqual(v, 525)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    def test_print_4(self):
        w = StringIO()
        collatz_print(w, 3, 33, 112)
        self.assertEqual(w.getvalue(), "3 33 112\n")

    def test_print_5(self):
        w = StringIO()
        collatz_print(w, 100, 250, 128)
        self.assertEqual(w.getvalue(), "100 250 128\n")

    def test_print_6(self):
        w = StringIO()
        collatz_print(w, 1, 900000, 525)
        self.assertEqual(w.getvalue(), "1 900000 525\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        r = StringIO("3 33\n100 250\n1 900000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "3 33 112\n100 250 128\n1 900000 525\n")

    def test_solve_2(self):
        r = StringIO("10 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 20 21\n")

    def test_solve_3(self):
        r = StringIO("12 14\n9 100\n7 77\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "12 14 18\n9 100 119\n7 77 116\n")

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
Ran 22 tests in 11.617s
OK


$ coverage report -m                   >> TestCollatz.out



$ cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 22 tests in 11.617s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Collatz.py          34      0     12      0   100%
TestCollatz.py      95      0      0      0   100%
------------------------------------------------------------
TOTAL              129      0     12      0   100%
"""
