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

    # corner cases

    # 3 input values
    def test_read_4(self):
        s = "1 10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # 4 input values
    def test_read_5(self):
        s = "1 10 1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    

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

    # corner cases
    #reverse order
    def test_eval_5(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20) 

    #large range
    def test_eval_6(self):
        v = collatz_eval(1234, 43214)
        self.assertEqual(v, 324)
    

    def test_eval_7(self):
        v = collatz_eval(439, 92)
        self.assertEqual(v, 144)

    #same number
    def test_eval_8(self):
        v = collatz_eval(8, 8)
        self.assertEqual(v, 4)

    #testing range() implementation
    def test_eval_9(self):
        v = collatz_eval(5, 6)
        self.assertEqual(v, 9)

    #testing big numbers
    def test_eval_10(self):
        v = collatz_eval(1, 100000)
        self.assertEqual(v, 351)

    def test_eval_11(self):
        v = collatz_eval(869222, 869573)
        self.assertEqual(v, 388)

    def test_eval_12(self):
        v = collatz_eval(431700, 431055)
        self.assertEqual(v, 312)
    
    #testing 1
    def test_eval_13(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_14(self):
        v = collatz_eval(984263, 984008)
        self.assertEqual(v, 352)

    def test_eval_15(self):
        v = collatz_eval(884741, 885879)
        self.assertEqual(v, 370)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # corner cases
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 8, 8, 4)
        self.assertEqual(w.getvalue(), "8 8 4\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")
    
    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # corner cases
    # too many numbers in one line, should not affect that line nor any
    # future lines (same output)
    def test_solve_2(self):
        r = StringIO("10 1 20\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "10 1 20\n100 200 125\n201 210 89\n900 1000 174\n")
    


    

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
