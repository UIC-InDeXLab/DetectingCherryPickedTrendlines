# Abolfazl Asudeh,  http://asudeh.github.io

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

# -----------------------------------------------------------------------------------
def mylog(st, outputfile):
    outfile = open(outputfile, 'a');
    outfile.write(st + '\n');
    outfile.close();

# -----------------------------------------------------------------------------------
n = None;  # database size
d = None;  # number of attributes (|D|)
data = None; # The first d attributes are trend attributes, the last is the objective value y
col = [] # The NAMES of the columns
B = None; # the index of the poins in Beginning
E = None; # the index of the points in End

debugmod = 'on'  # type: string; turns the debug mode on and off


def load_from_csv(dataset, columns, headerIndex=0, nrows=-1, datecols=None):
        global data,n,d, col
        filename = dataset
        col = columns # the last one is the objective value
        if datecols is None:  data = pd.read_csv(filename,usecols = columns ,header=headerIndex) if nrows==-1 else pd.read_csv(filename, usecols = columns,header=headerIndex,nrows=nrows)
        else: data = pd.read_csv(filename,usecols = columns ,header=headerIndex, parse_dates=datecols) if nrows==-1 else pd.read_csv(filename, usecols = columns,header=headerIndex,nrows=nrows,parse_dates=datecols)
        n = len(data)
        d = len(columns) - 1
        # print data

def RoI_S(Bconds, Econds):
        global B, E
        st = "SELECT * FROM data"
        first = True
        for i in range(len(Bconds)):
                if Bconds[i][0] is not None:
                        if first:
                             st+= " WHERE " + col[i] + ">=" + str(Bconds[i][0])
                             first = False
                        else:   st+= " AND " + col[i] + ">=" + str(Bconds[i][0])
                if Bconds[i][1] is not None:
                        if first:
                             st+= " WHERE " + col[i] + "<=" + str(Bconds[i][1])
                             first = False
                        else:   st+= " AND " + col[i] + "<=" + str(Bconds[i][1])
        #print st
        B = query(st)
        st = "SELECT * FROM data"
        first = True
        for i in range(len(Econds)):
                if Econds[i][0] is not None:
                        if first:
                             st+= " WHERE " + col[i] + ">=" + str(Econds[i][0])
                             first = False
                        else:   st+= " AND " + col[i] + ">=" + str(Econds[i][0])
                if Econds[i][1] is not None:
                        if first:
                             st+= " WHERE " + col[i] + "<=" + str(Econds[i][1])
                             first = False
                        else:   st+= " AND " + col[i] + "<=" + str(Econds[i][1])
        # print st
        E = query(st)

# ------------------- Private functions ---------------------------
def query(querystring):
        #print(querystring + ", cost = "+str(cost))
        T = pysqldf(querystring)
        return T

'''
#Test
load_from_csv("data/Wine.csv",["Rank","Vintage","Score","Price"])
#print data[1:10]
RoI_S([(None,None),(None,None),(None,None),(None,20)], [(None,None),(None,None),(None,None),(60,None)])
print B
print E
'''










