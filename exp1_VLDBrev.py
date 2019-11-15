import Support
from Support import *
import basestuff
from basestuff import *
from time import time

'''
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

# ------- CO2 ------------
print 'CO2:'
filename = "data/co2-ppm-daily.csv"
datecols = ['date']
for n in [2000,4000,6000,8000,10000]:
    load_from_csv(filename,columns = ['date','value'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support(-100,100)
    t1=time()-t
    t = time()
    support_baseline(-100,100)
    t2=time()-t
    print basestuff.n,'t1',t1,'t2',t2

for n in [2000,4000,6000,8000,10000]:
    load_from_csv(filename,columns = ['date','value'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support_ordered_enum(-100,100)
    t3=time()-t
    print basestuff.n,'t3',t3
print "--------------------------"
'''

# ------- wether ------------
print 'wether:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for n in [20000,30000,40000,50000]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support(-1,1)
    t1=time()-t
    print t1
    t = time()
    #support_baseline(-1,1)
    t2=time()-t
    t = time()
    support_ordered_enum(-1,1)
    t3=time()-t
    print basestuff.n,t1,t2,t3
print "--------------------------"

# ------- DoT ------------
print 'DoT:'
filename = "data/DOTDec2017.csv"
#n=1000
for n in [100000,200000,300000,400000,500000]:
    load_from_csv(filename,columns = ['ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID','DISTANCE'],nrows=n)
    RoI_Split()
    t = time()
    support(-100,100)
    t1=time()-t
    t = time()
    support_baseline(-1,1)
    t2=time()-t
    t = time()
    #support_ordered_enum(-100,100)
    t3=time()-t
    print basestuff.n,t1,t2,t3
print "--------------------------"

# ------- DoT2 ------------
print 'DoT Baseline:'
filename = "data/DOTDec2017.csv"
#n=1000
for n in [100000,200000,300000,400000,500000]:
    load_from_csv(filename,columns = ['ORIGIN_AIRPORT_ID','DEST_AIRPORT_ID','DISTANCE'],nrows=n)
    RoI_Split()
    t = time()
    support_baseline(-100,100)
    t2=time()-t
    print basestuff.n,t2
print "--------------------------"


# ------- Stock ------------
print 'stock:'
#load_from_csv("data/stock_sample.csv",["ticker","open","close","low","high","volume","date"])
datecols = ['date']
filename = "data/historical_stock_prices.csv"
#n=1000
for n in [100,1000,10000]:
    load_from_csv(filename,["date","close"],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support(-1,1)
    t1=time()-t
    t = time()
    support_baseline(-1,1)
    t2=time()-t
    t = time()
    support_ordered_enum(-1,1)
    t3=time()-t
    print basestuff.n,t1,t2,t3
for n in [100000,1000000,10000000]:
    load_from_csv(filename,["date","close"],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support(-1,1)
    t1=time()-t
    print basestuff.n,t1
print "--------------------------"

#RoI_S([(None,"'2013-08-02 0:00'")], [("'2013-08-03 0:00'",None)])


#for i in range(10):
#print support_rand(10, 50, 10)s
