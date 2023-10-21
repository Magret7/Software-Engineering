# ------
# Count.py
# ------

# count(start, [step])


def count_while(start, *step):
   if not step :
      s = 1
   else :
      s = step[0]
   n = start
   while True:
      yield n
      n += s

