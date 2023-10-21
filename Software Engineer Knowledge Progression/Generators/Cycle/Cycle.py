from itertools import cycle

# ------
# Cycle.py
# ------

def cycle_range_for(n) :
    if n :
        while True :
            for i in range(len(n)) :
                yield n[i]
    else :
        pass

def cycle_for (n) : # uner-defined iterable
    p = iter(n)
    try :
        next(p)
    except StopIteration:
        return
    p = iter(n)
    while True :
        try :
            while True :
                w = next(p)
                yield w
        except StopIteration :
            p = iter(n)

