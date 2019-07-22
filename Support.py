# Abolfazl Asudeh, http://asudeh.github.io

import basestuff
from basestuff import *
import red_black_tree
from red_black_tree import *
import numpy as np

def support_baseline(low, high):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    sup = 0.
    for b in B:
        for e in E:
            tmp = e-b
            if tmp>=low and tmp<=high: sup+=1
    return sup/(len(B)*len(E))

def support(low, high):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    #print 'len(B), len(E): ', len(B), len(E)
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    sup = 0.
    for b in B:
        Fl = Bsearch(b+low,E)
        Fh = Bsearch(b+high,E)
        sup+=Fh-Fl
    return sup/(len(B)*len(E))

def support_rand_baseline(low, high, budget):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
    Rb = np.random.randint(len(B), size=budget)
    Re = np.random.randint(len(E), size=budget)
    sup = 0.
    for i in range(budget):
        tmp = E[Re[i]]-B[Rb[i]]
        if tmp>=low and tmp<=high: sup+=1
    return sup/budget

def support_rand(low, high, budget):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
    Rb = np.random.randint(len(B), size=budget)
    Ep = sorted(E[np.random.randint(len(E), size=budget)])
    sup = 0.
    for i in range(budget):
        Fl = Bsearch(B[Rb[i]]+low,Ep)
        Fh = Bsearch(B[Rb[i]]+high,Ep)
        sup+=Fh-Fl
    return sup/(budget**2)

def support_constrainted(low, high, window):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = sorted(basestuff.E[col[d]])
    #print 'len(B), len(E): ', len(B), len(E)
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    sup = 0.
    rbt = RedBlackTree()
    for i in range(window): rbt.insert(E[i])
    i = 0
    for b in B:
        F1 = rbt.searchTree_smallercnt(b+low,window)
        F2 = rbt.searchTree_smallercnt(b+high,window)
        sup+=F2-F1
        rbt.delete_node(E[i])
        if(i+window<len(E)): rbt.insert(E[i+window])
        i+=1
    return sup/(len(B)*window)


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
    while l<len(S) and S[l] == x: l+=1
    return l



