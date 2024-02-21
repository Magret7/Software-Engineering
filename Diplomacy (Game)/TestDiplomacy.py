#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-assert-stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_read, diplomacy_eval, diplomacy_print, diplomacy_solve

# -----------
# TestCollatz
# -----------


class TestDiplomacy (TestCase):
    # ----
    # read
    # ----
    def test_read_1(self):
        s = StringIO("A Madrid Hold\nB Barcelona Move Madrid")
        i = diplomacy_read(s)
        self.assertEqual(i, ['A Madrid Hold', 'B Barcelona Move Madrid'])

    def test_read_2(self):
        s = StringIO("A Madrid Hold")
        i = diplomacy_read(s)
        self.assertEqual(i, ['A Madrid Hold'])

    def test_read_3(self):
        s = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B")
        i = diplomacy_read(s)
        self.assertEqual(i, ['A Madrid Hold', 'B Barcelona Move Madrid', 'C London Support B'])
    
    
    # ----
    # eval
    # ----
    def test_eval_1(self):
        v = diplomacy_eval(['A Madrid Hold', 'B Barcelona Move Madrid'])
        self.assertEqual(v, ['A [dead]', 'B [dead]'])

    def test_eval_2(self):
        v = diplomacy_eval(['A Madrid Hold'])
        self.assertEqual(v, ['A Madrid'])
                        
    def test_eval_3(self):
        v = diplomacy_eval(['A Madrid Hold', 'B Barcelona Move Madrid', 'C London Support B'])
        self.assertEqual(v, ['A [dead]', 'B Madrid', 'C London'])


    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        diplomacy_print(w, ['A [dead]', 'B [dead]'])
        self.assertEqual(w.getvalue(), 'A [dead]\nB [dead]')
        
    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, ['A Madrid'])
        self.assertEqual(w.getvalue(), 'A Madrid')
        
    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, ['A [dead]', 'B Madrid', 'C London'])
        self.assertEqual(w.getvalue(), 'A [dead]\nB Madrid\nC London')


    # -----
    # solve
    # -----
    
    #Located issues
    def test_solve_1(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]")
   
    def test_solve_2(self):
        r = StringIO("A Madrid Hold")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A Madrid")

    def test_solve_3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC London")

# ----
# main
# ----

if __name__ == "__main__": # pragma: no cover
    main()


""" #pragma: no cover
$ coverage run --branch TestDiplomacy.py >  TestDiplomacy.out 2>&1


$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestDiplomacy.out



$ cat TestDiplomacy.out
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
