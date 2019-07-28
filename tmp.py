import Support
from Support import *
import basestuff
from basestuff import *
from time import time

print 'wether vary n - most supported statement:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for n in [2000,4000,6000,8000,10000]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    v = MostSupportedStatement(30)
    t1=time()-t
    print basestuff.n,v[0],t1
print "--------------------------"