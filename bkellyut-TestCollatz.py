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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle, is_odd, Cache


# -----------
# TestCollatz
# -----------


class TestCollatz (TestCase):
    # ----
    # read
    # ----

    def test_read1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2(self):
        s = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)
    
    def test_read3(self):
        s = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  201)
        self.assertEqual(j, 210)

    def test_read4(self):
        s = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    # ----
    # eval
    # ----

    def test_base_case_eval(self):
        v = collatz_eval(1,1)
        self.assertEqual(v, 1)

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
        v = collatz_eval(568, 639)
        self.assertEqual(v, 132)

    def test_eval_6(self):
        v = collatz_eval(238, 476)
        self.assertEqual(v, 144)

    def test_eval_7(self):
        v = collatz_eval(6, 2543)
        self.assertEqual(v, 209)

    def test_eval_sub_1(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_sub_2(self):
        v = collatz_eval(476, 238)
        self.assertEqual(v, 144)
    
    def test_eval_sub_3(self):
        v = collatz_eval(2543, 6)
        self.assertEqual(v, 209)

    # -----
    # print
    # -----

    def test_print1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print4(self):
        w = StringIO()
        collatz_print(w, 9000, 1000, 174)
        self.assertEqual(w.getvalue(), "9000 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO("900 1000\n568 638\n238 476\n2860 3574\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "900 1000 174\n568 638 132\n238 476 144\n2860 3574 217\n")

    def test_solve3(self):
        r = StringIO("6 2543\n6455 7055\n1466 7433\n631 1755\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "6 2543 209\n6455 7055 257\n1466 7433 262\n631 1755 182\n")

    def test_solve4(self):
        r = StringIO("1465 3956\n1438 1614\n1106 1472\n8016 9426\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1465 3956 238\n1438 1614 172\n1106 1472 182\n8016 9426 260\n")

class TestGetCycle(TestCase):

    # ---------
    # get cycle 
    # ---------

    def test_get_cycle_1(self):
        cache = Cache()
        v = get_cycle(5, cache)
        self.assertEqual(v, 6)
    
    def test_get_cycle_2(self):
        cache = Cache()
        v = get_cycle(29, cache)
        self.assertEqual(v, 19)
    
    def test_get_cycle_3(self):
        cache = Cache()
        v = get_cycle(1, cache)
        self.assertEqual(v, 1)
    
    def test_get_cycle_4(self):
        cache = Cache()
        v = get_cycle(9, cache)
        self.assertEqual(v, 20)

class TestIsOdd(TestCase):

    # ------
    # is odd
    # ------

    def test_is_odd_1(self):
        self.assertTrue(is_odd(5))

    def test_is_odd_2(self):
        self.assertFalse(is_odd(2))

    def test_is_odd_3(self):
        self.assertTrue(is_odd(1))
        
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
