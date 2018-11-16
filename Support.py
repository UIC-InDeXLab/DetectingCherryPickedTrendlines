import basestuff
from basestuff import *
import numpy as np

def support_baseline(low, high):
    B = basestuff.B; E = basestuff.E; d = basestuff.d; col = basestuff.col
    sup = 0.
    for b in B:
        for e in E:
            tmp = e[col[d]]-b[col[d]]
            if tmp>=low and tmp<=high: sup+=1
    return sup/(len(B)*len(E))

def support(low, high):
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]]); d = basestuff.d; col = basestuff.col
    sup = 0.
    for b in B:
        Fl = Bsearch(b+low,S)
        Fh = Bsearch(b+high,S)
        sup+=Fh-Fl
    return sup

def Bsearch(x,S): # returns the index of the first item LARGER than x in S
    l = 0; h = len(S)
    while l<h:
        m = (l+h)/2
        if S[m]>x: h = m
        else: l = m
    return l



