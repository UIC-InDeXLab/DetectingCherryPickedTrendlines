# Abolfazl Asudeh, http://asudeh.github.io

import basestuff
from basestuff import *
import red_black_tree
from red_black_tree import *
import numpy as np
import math

def support_baseline(low, high):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
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

def support_rand_baseline(low, high, budget,reporterror=False):
    d = basestuff.d; col = basestuff.col
    Bp = list(basestuff.B[col[d]]); Ep = list(basestuff.E[col[d]])
    if len(Bp)==0 or len(Ep)==0: 
        print len(Bp), len(Ep)
        print 'Null ROI'
        return None
    Rb = np.random.randint(len(Bp), size=budget)
    Re = np.random.randint(len(Ep), size=budget)
    sup = 0.
    for i in range(budget):
        tmp = Ep[Re[i]]-Bp[Rb[i]]
        if tmp>=low and tmp<=high: sup+=1
    m = sup*1./budget
    error = 1.96*m*(m-1)/budget # z_0.025 = 1.96
    if not reporterror:
         return m
    return m,error

def support_rand(low, high, budget):
    d = basestuff.d; col = basestuff.col
    B = list(basestuff.B[col[d]]); E = list(basestuff.E[col[d]])
    Rb = np.random.randint(len(B), size=budget)
    indices = np.random.randint(len(E), size=budget)
    Ep = sorted([E[i] for i in indices])
    sup = 0.
    for i in range(budget):
        Fl = Bsearch(B[Rb[i]]+low,Ep)
        Fh = Bsearch(B[Rb[i]]+high,Ep)
        sup+=Fh-Fl
    return sup/(budget**2)

def support_constrainted(low, high, window,baseline=False):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
    #print 'len(B), len(E): ', len(B), len(E)
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    sup = 0.
    if baseline==True or window<=10*(math.log(len(E))/math.log(2)):
        i = 0
        for b in B:
            for e in E[i:min(i+window,len(E)-1)]:
                tmp = e-b
                if tmp>=low and tmp<=high: sup+=1
    else:
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

def support_rand_constrained(low, high, window, budget):
    d = basestuff.d; col = basestuff.col
    Bp = list(basestuff.B[col[d]]); Ep = list(basestuff.E[col[d]])
    if len(Bp)==0 or len(Ep)==0: 
        print len(Bp), len(Ep)
        print 'Null ROI'
        return None
    Rb = np.random.randint(len(Bp), size=budget)
    WRand = np.random.randint(window, size=budget)
    sup = 0.
    for i in range(budget):
        j = WRand[i] + Rb[i] if WRand[i] + Rb[i]<len(Ep) else WRand[i]%(len(Ep)-Rb[i])+Rb[i]
        tmp = Ep[j]-Bp[Rb[i]]
        if tmp>=low and tmp<=high: sup+=1
    return sup/budget

def tightest_statement(supportval): # 0<supportval<1
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    l = [0]*(len(B)*len(E))
    i=0
    for b in B:
        for e in E:
            l[i]=e-b
            i+=1
    l = sorted(l)
    delta = int(supportval * len(l))
    min = 1000000. # infinity
    Statement = None
    for i in range(len(l) - delta-1):
        if min>l[i+delta]-l[i]:
            Statement = (l[i],l[i+delta])
    return Statement

def MostSupportedStatement(delta):
    d = basestuff.d; col = basestuff.col
    B = basestuff.B[col[d]]; E = basestuff.E[col[d]]
    if len(B)==0 or len(E)==0: 
        print len(B), len(E)
        print 'Null ROI'
        return None
    l = [0]*(len(B)*len(E))
    i=0
    for b in B:
        for e in E:
            l[i]=e-b
            i+=1
    l = sorted(l)
    max = 0; Statement = None
    for i in range(len(l)):
        j=Bsearch(l[i]+delta,l,True)
        if j==-1: break
        if max < (j-i):
            max = j-i
            Statement = (l[i],l[j])
    return max*1./len(l),Statement

# --------------------- Private -------------------------
def Bsearch(x,S,retnegone=False): # returns the index of the first item LARGER than x in S
    # retnegone is a flag to say that the function should return -1 if the key is not in the range
    l = 0; h = len(S)-1
    # print "low: ", l, ", high: ", h
    if retnegone and x>S[len(S)-1] or x<S[0]: return -1
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



