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
    t = time()
    v = tightest_statement(.9)
    t1=time()-t
    print city, .9,v,v[1]-v[0],t1
    spt +=v[1]-v[0]
print spt/len(cities)
