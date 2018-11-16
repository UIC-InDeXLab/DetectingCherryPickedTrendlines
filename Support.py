# Abolfazl Asudeh, http://asudeh.github.io

import basestuff
from basestuff import *
import numpy as np

def support_baseline(low, high):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]]);
    sup = 0.
    for b in B:
        for e in E:
            tmp = e-b
            if tmp>=low and tmp<=high: sup+=1
    return sup/(len(B)*len(E))

def support(low, high):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    sup = 0.
    for b in B:
        Fl = Bsearch(b+low,E)
        Fh = Bsearch(b+high,E)
        sup+=Fh-Fl
    return sup/(len(B)*len(E))

def support_rand_baseline(low, high, budget):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    Rb = np.random.randint(len(B), size=budget)
    Re = np.random.randint(len(E), size=budget)
    sup = 0.
    for i in range(budget):
        tmp = E[Re[i]]-B[Rb[i]]
        if tmp>=low and tmp<=high: sup+=1
    return sup/budget

def support_rand(low, high, budget):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    return


# --------------------- Private -------------------------
def Bsearch(x,S): # returns the index of the first item LARGER than x in S
    l = 0; h = len(S)-1
    # print "low: ", l, ", high: ", h
    while l<h:
        m = (l+h)/2
        # print "low: ", l, ", high: ", h, ", mid: ", m
        if S[m]>x: h = m-1
        elif S[m]<x: l = m+1
        else: 
            l = m+1
            break
    while S[l] == x: l+=1
    return l



