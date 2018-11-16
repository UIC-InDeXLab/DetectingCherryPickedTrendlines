import Support
from Support import *
import basestuff
from basestuff import *

load_from_csv("data/Wine.csv",["Rank","Vintage","Score","Price"])
RoI_S([(None,None),(None,None),(None,95)], [(None,None),(None,None),(96,None)])
print support_baseline(10,50)