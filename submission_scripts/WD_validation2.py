import Support
from Support import *
import basestuff
from basestuff import *
from time import time

cities = ['Vancouver','Portland','San Francisco','Seattle','Los Angeles','San Diego','Las Vegas','Phoenix','Albuquerque','Denver','San Antonio','Dallas','Houston','Kansas City','Minneapolis','Saint Louis','Chicago','Nashville','Indianapolis','Atlanta','Detroit','Jacksonville','Charlotte','Miami','Pittsburgh','Toronto','Philadelphia','New York','Montreal','Boston','Beersheba','Tel Aviv District','Eilat','Haifa','Nahariyya','Jerusalem']
spt = 0.
datecols = ['datetime']
for city in cities:
    columns = ["datetime",city]
    load_from_csv("data/temperature.csv",columns,datecols=datecols)
    RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
    sup = support(-500,0.0001)
    print city, sup
    spt +=sup
print spt/len(cities)

'''
columns = ["datetime","Detroit"]
#dtypes = {'datetime': np.datetime64, 'Detroit': np.float64}
datecols = ['datetime']
load_from_csv("data/temperature.csv",columns,datecols=datecols)
# load_from_csv("data/temperature.csv",columns,datecols=datecols)
# print basestuff.data.dtypes
RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
# RoI_S([(np.datetime64('2012-12-01 00:00'),np.datetime64('2013-03-01 00:00'))], [(np.datetime64('2012-06-01 00:00'),np.datetime64('2012-09-01 00:00'))])
t = time()
print support(-500,0.1)
'''

'''
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
'''