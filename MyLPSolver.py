import numpy as np;
from scipy.optimize import linprog
import basestuff
import math

Opt = None; # general optimization factor
bounds = None;

def solve(c = None, A_ub=None,b_ub=None,A_eq=None, b_eq=None,bnds=None):
    global Opt,bounds;

    if Opt is None:
        tmp =[0 for i in range(basestuff.d-1)];
        tmp.append(1);
        Opt = np.array(tmp);
        #tmp[basestuff.d-1]=0
        #tmp2 = [math.pi/2 for i in range(basestuff.d-1)]
        #bounds=  np.array([tmp,tmp2]).T

    res = linprog(Opt if c is None else c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds = bnds, options={"disp": False})
    return [res.success,res.x]
