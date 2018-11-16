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
for i in range(10):
    v1 = np.var([support_rand_baseline(10, 50, 10) for j in range(10)])
    v2 = np.var([support_rand(10, 50, 10) for j in range(10)])
    print 'baseline: ', v1, 'smart: ', v2

#for i in range(10):
#    print support_rand(10, 50, 10)