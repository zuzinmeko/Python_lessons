# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:16:58 2021

@author: hp
"""

from math import sinh, exp, e, pi
x = 2*pi
r1 = sinh(x)
r2 = 0.5*(exp(x) - exp(-x))
r3 = 0.5*(e**x - e**(-x))
print('%.16f %.16f %.16f' % (r1,r2,r3))