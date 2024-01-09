from mpmath import mp
from math import *
from itertools import count

mp.dps = 100000
e_gen_1 = 0
for i in count(0):
    e_gen_2 = e_gen_1
    e_gen_1 = e_gen_1 + (1/mp.factorial(i))
    if e_gen_1 == e_gen_2:
        file1 = open("output.txt", "w")
        file1.write(str(e_gen_1))
        file1.close()
        break
    
