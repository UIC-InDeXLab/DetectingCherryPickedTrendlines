import Support
from Support import *
import basestuff
from basestuff import *
from time import time


# ------- wether ------------
print 'wether vary support - tightest statement:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for support in [.1,.2,.3,.4,.5,.6,.7,.8,.9]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols)
    RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
    t = time()
    v = tightest_statement(support)
    t1=time()-t
    print basestuff.n,support,v,v[1]-v[0],t1
print "--------------------------"

# ------- wether ------------
print 'wether vary delta - most supported statement:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for delta in [15,20,25,30,35]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols)
    RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
    t = time()
    v = MostSupportedStatement(delta)
    t1=time()-t
    print basestuff.n,delta,v,t1
print "--------------------------"

# ------- wether ------------
print 'wether vary n - tightest statement:'
datecols = ['datetime']
filename = "data/temperature.csv"
#n=1000
for n in [2000,4000,6000,8000,10000]:
    load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols,nrows=n)
    RoI_Split()
    t = time()
    v = tightest_statement(.8)
    t1=time()-t
    print basestuff.n,v[1]-v[0],t1
print "--------------------------"

# ------- wether ------------
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
