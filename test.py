import Support
from Support import *
import basestuff
from basestuff import *
from time import time
filename = "data/brent-daily.csv"
datecols = ['Date']
load_from_csv(filename,columns = ['Date','Price'],datecols=datecols,nrows=10000)
RoI_Split()
#print tightest_statement(.8)
print MostSupportedStatement(20)

'''
t = time()
print support_baseline(10,50)
print time()-t
print support_constrainted(10,50,100,baseline=True)
t = time()
print support(10,50)
print time()-t
for i in range(10):
    v1 = np.var([support_rand_baseline(10, 50, 10) for j in range(10)])
    v2 = np.var([support_rand(10, 50, 10) for j in range(10)])
    print 'baseline: ', v1, 'smart: ', v2

#for i in range(10):
#    print support_rand(10, 50, 10)
'''