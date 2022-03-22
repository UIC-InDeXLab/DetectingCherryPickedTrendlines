import Support
from Support import *
import basestuff
from basestuff import *
from time import time

# ------- Oil ------------
print 'Oil:'
filename = "data/brent-daily.csv"
datecols = ['Date']
for n in [2000,4000,6000,8000,10000]:
    load_from_csv(filename,columns = ['Date','Price'],datecols=datecols,nrows=n)
    RoI_Split()
    print basestuff.n

    t = time()
    print support(-3,3)
    t1=time()-t

    t = time()
    print support_baseline(-3,3)
    t2=time()-t

    t = time()
    print support_ordered_enum(-3,3)
    t3=time()-t
    
    print t1,t2,t3
print "--------------------------"
