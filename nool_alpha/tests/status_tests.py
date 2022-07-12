import sys
sys.path.append('C://Users//mahmoud//projects//')
sys.path.append('C://Users//mahmoud//projects\\nool_alpha\\nool')

import random
import math

import nool_alpha.nool
import nool_alpha.nool.items
from items import *
import nool_alpha.nool.status
from status import *

testchar = Plunger("TEST", 5, mage, "E")
def stats_check(char):
    return char.maxhp
    return char.maxmp
    return char.str
    return char.dex
    return char.int
    return char.acc
    return char.speed
    return char.job
    return char.race
    return char.totalExp
    return char.active
    return char.alive
    return char.tick
    return char.inflict
print (stats_check(testchar))
