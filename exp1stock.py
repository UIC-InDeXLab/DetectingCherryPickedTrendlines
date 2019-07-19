import Support
from Support import *
import basestuff
from basestuff import *
from time import time

#load_from_csv("data/stock_sample.csv",["ticker","open","close","low","high","volume","date"])
datecols = ['date']
load_from_csv("data/stock_sample.csv",["date","close"],datecols=datecols)

RoI_S([(None,"'2013-08-02 0:00'")], [("'2013-08-03 0:00'",None)])
t = time()
print support(-10,0)
#print time()-t

#for i in range(10):
#print support_rand(10, 50, 10)s