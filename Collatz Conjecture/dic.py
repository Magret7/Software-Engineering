
import random  

# define the function
def collatz_sequence(x):
    # create an empty list
    list_ = []
    count = 1
    # while the no is not equal to 1 loop
    while x > 1 :
        if (x % 2) == 0 :
             x = (x // 2)
        else :
            x = (3 * x) + 1
        count += 1  
    list_.append(count)
    return list_
    
# create an dictionary
Dict = {}

for i in range(1,50000):
    num = random.randint(1, 999999)
    if num not in Dict:
        list_val = collatz_sequence(int(num))
        Dict.setdefault(num,[]).extend(list_val)

print(Dict)







