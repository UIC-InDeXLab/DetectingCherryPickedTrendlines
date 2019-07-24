import Support
from Support import *
import basestuff
from basestuff import *
from time import time

# ------- Stock ------------
print 'stock:'
#load_from_csv("data/stock_sample.csv",["ticker","open","close","low","high","volume","date"])
datecols = ['date']
filename = "data/historical_stock_prices.csv"
#n=1000
bdg = 10000
for n in [2000000,4000000,6000000,8000000,10000000]:
    load_from_csv(filename,["date","close"],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    s = support(-5,5)
    t1=time()-t
    t = time()
    s2,e = support_rand_baseline(-5,5, bdg,True)
    t2=time()-t
    print basestuff.n,s,s2,e,t1,t2
print "--------------------------"
