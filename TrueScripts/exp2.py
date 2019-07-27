import Support
from Support import *
import basestuff
from basestuff import *
from time import time

# ------- CO2 vary window ------------
print 'CO2 vary window'
filename = "data/co2-ppm-daily.csv"
datecols = ['date']
for window in [10,100,1000,5000]:
    load_from_csv(filename,columns = ['date','value'],datecols=datecols)
    RoI_Split()
    t = time()
    support_constrainted(-100,100,window,baseline=True)
    t1=time()-t
    t = time()
    support_constrainted(-100,100,window)
    t2=time()-t
    print basestuff.n,window,t1,t2
print "--------------------------"


# ------- wether ------------
print 'wether vary window:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for window in [10,100,1000,5000]:
#for window in [1000,10000]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols,nrows=20000)
    RoI_Split()
    t = time()
    support_constrainted(-1,1,window,baseline=True)
    t1=time()-t
    t = time()
    support_constrainted(-1,1,window)
    t2=time()-t
    print basestuff.n,window,t1,t2
print "--------------------------"



# ------- CO2 vary n ------------
print 'CO2 vary n'
filename = "data/co2-ppm-daily.csv"
datecols = ['date']
for n in [5000,10000,15000,20000]:
    load_from_csv(filename,columns = ['date','value'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support_constrainted(-100,100,1000,baseline=True)
    t1=time()-t
    t = time()
    support_constrainted(-100,100,1000)
    t2=time()-t
    print basestuff.n,'1000',t1,t2
print "--------------------------"


# ------- wether ------------
print 'wether vary n:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for n in [10000,20000,30000,40000,50000]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    support_constrainted(-1,1,1000,baseline=True)
    t1=time()-t
    t = time()
    support_constrainted(-1,1,1000)
    t2=time()-t
    print basestuff.n,1000,t1,t2
print "--------------------------"
