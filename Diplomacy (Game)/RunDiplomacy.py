#!/usr/bin/env python3

# ------------------------------
# projects/Diplomacy/RunDiplomacy.py
# Copyright (C)
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

from Diplomacy import diplomacy_solve

# ----
# main
# ----

if __name__ == "__main__":
    diplomacy_solve(sys.stdin, sys.stdout)

""" #pragma: no cover
$ cat RunDiplomacy.in
1 10




$ python RunDiplomacy.py < RunDiplomacy1.in > RunDiplomacy1.out

$ cat RunDiplomacy.out
1 10 1




$ python -m pydoc -w Diplomacy
# That creates the file Diplomacy.html
"""
