from itertools import repeat

# ------
# Repeat.py
# ------

def repeat_while(x,*y):
    if not y :
        while True:
            yield x
    else:
        times = y[0]
        for i in range(times):
            yield x
        