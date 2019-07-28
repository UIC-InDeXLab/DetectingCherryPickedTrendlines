import Support
from Support import *
import basestuff
from basestuff import *
from time import time

budget = [10,20,30,40,50,60,70,80,90,100]
agg = 30
# ------- weather ------------
print 'weather:'
datecols = ['datetime']
filename = "data/temperature.csv"
load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols)
RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
V0_agg=[0 for i in range(len(budget))];V1_agg=[0 for i in range(len(budget))];V2_agg=[0 for i in range(len(budget))]
rngs = [(17.87, 48.97)]
a, b = rngs[0]
for j in range(len(budget)):
    for iter in range(agg):
        v0_sum = 0
        v1_sum = 0
        v2_sum = 0
        for i in range(agg):
            v0 = np.var([support_rand_baseline(a, b, budget[j]) for k in range(agg)])
            v1 = np.var([support_rand_baseline(a, b, int(budget[j]*math.log(budget[j])/math.log(2))) for k in range(agg)])
            v2 = np.var([support_rand(a, b, budget[j]) for k in range(agg)])
            #print 'baseline: ', v1, 'smart: ', v2
            v0_sum+=v0; v1_sum+=v1; v2_sum+=v2
        V0_agg[j]+=v0_sum*1./agg
        V1_agg[j]+=v1_sum*1./agg; 
        V2_agg[j]+=v2_sum*1./agg; 
    print V0_agg[j]*1./agg,V1_agg[j]*1./agg,V2_agg[j]*1./agg
print "--------------------------"
