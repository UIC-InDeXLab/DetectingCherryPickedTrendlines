import Support
from Support import *
import basestuff
from basestuff import *
from time import time
filename = "data/brent-daily.csv"
datecols = ['Date']
load_from_csv(filename,columns = ['Date','Price'],datecols=datecols,nrows=1000)
RoI_Split()
#print tightest_statement(.8)
#print MostSupportedStatement(20)
#print support_baseline(10,50)
print support(10,50)
print support_rand_baseline(10, 50, 10,True)
print support_rand_constrained(10, 50, 100,10)
#print support_rand_baseline(10, 50, 10)

for j in [10,50,100,500,1000]:
    r = [support_rand_baseline(-20,20, j) for k in range(20)]
    #for v in r: print v
    print j, np.var([support_rand_baseline(-20,20, j) for k in range(20)])
    print j, np.var([support_rand(-20,20, j) for k in range(20)])
    print '--------------------------'