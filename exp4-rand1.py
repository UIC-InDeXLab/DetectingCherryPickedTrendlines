import Support
from Support import *
import basestuff
from basestuff import *
from time import time

agg = 30
'''
# ------- CO2 ------------
print 'CO2:'
filename = "data/co2-ppm-daily.csv"
datecols = ['date']
load_from_csv(filename,columns = ['date','value'],datecols=datecols)
RoI_Split()
V1_agg=[0,0,0,0,0];V2_agg=[0,0,0,0,0]
rngs = [(-10,10),(-20,20),(-30,30),(-35,35),(-40,40)] # supports: .32,.58,.77,.85,.91
for j in range(5):
    for iter in range(agg):
        v1_sum = 0
        v2_sum = 0
        a, b = rngs[j]
        for i in range(agg):
            r1 = [support_rand_baseline(a, b, agg) for k in range(agg)]
            v1 = np.var(r1)
            r2 = [support_rand(a, b, agg) for k in range(agg)]
            v2 = np.var(r2)
            #print 'baseline: ', v1, 'smart: ', v2
            v1_sum+=v1; v2_sum+=v2
        V1_agg[j]+=v1_sum*1./agg; 
        V2_agg[j]+=v2_sum*1./agg; 
    print V1_agg[j]*1./agg,V2_agg[j]*1./agg
print "--------------------------"
'''

# ------- weather ------------
print 'weather:'
datecols = ['datetime']
filename = "data/temperature.csv"
load_from_csv(filename,columns = ["datetime",'New York'],datecols=datecols)
RoI_S([("'2012-12-01 0:00'","'2013-03-01 0:00'")], [("'2013-06-01 0:00'","'2013-09-01 0:00'")])
V1_agg=[0,0,0,0,0,0];V2_agg=[0,0,0,0,0,0]
rngs = [(30.23, 48.97), (24.96, 48.97),(21.37, 48.97),(17.87, 48.97),(12.858, 48.97),(8, 50)]
for j in range(6):
    for iter in range(agg):
        v1_sum = 0
        v2_sum = 0
        a, b = rngs[j]
        for i in range(agg):
            r1 = [support_rand_baseline(a, b, agg) for k in range(agg)]
            v1 = np.var(r1)
            r2 = [support_rand(a, b, agg) for k in range(agg)]
            v2 = np.var(r2)
            #print 'baseline: ', v1, 'smart: ', v2
            v1_sum+=v1; v2_sum+=v2
        V1_agg[j]+=v1_sum*1./agg; 
        V2_agg[j]+=v2_sum*1./agg; 
    print V1_agg[j]*1./agg,V2_agg[j]*1./agg
print "--------------------------"

'''
for rng in [(30.23, 48.97), (24.96, 48.97),(21.37, 48.97),(17.87, 48.97),(12.858, 48.97),(8, 50)]:
    v1_sum = 0; avg1_sum=0
    v2_sum = 0; avg2_sum=0
    for i in range(agg):
        a, b = rng
        r1 = [support_rand_baseline(a, b, agg) for j in range(agg)]
        v1 = np.var(r1); avg1 = np.mean(r1)
        r2 = [support_rand(a, b, agg) for j in range(agg)]
        v2 = np.var(r2); avg2 = np.mean(r2)
        #print 'baseline: ', v1, 'smart: ', v2
        v1_sum+=v1; avg1_sum+=avg1
        v2_sum+=v2; avg2_sum+=avg2
    print rng,avg1_sum*1./agg, avg2_sum*1./agg, v1_sum*1./agg, v2_sum*1./agg
print "--------------------------"
'''