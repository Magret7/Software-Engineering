from itertools import chain

# ------
# Chain.py
# ------

def chain_for(*x) :
   if x :
      for i in x :
         for j in i :
            yield j
   else :
      pass    
       
def chain_generator(*x) :
   if x :
      return (j for i in x for j in i)
   else :
      pass

