import Support
from Support import *
import basestuff
from basestuff import *
from time import time

load_from_csv("data/Wine.csv",["Rank","Vintage","Score","Price"])
RoI_S([(None,None),(None,None),(None,95)], [(None,None),(None,None),(96,None)])
t = time()
print support_baseline(10,50)
print time()-t
t = time()
print support(10,50)
print time()-t
for i in range(5):
    print support_rand_baseline(10, 50, 10)