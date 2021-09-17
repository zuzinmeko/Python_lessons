# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:16:40 2021

@author: hp
"""

from math import sin, cos,pi
x = pi*1/4
val_1= sin(x)**2 + cos(x)**2
print(val_1)


v0 = 3 
t = 1
a = 2
s = v0*t + 0.5*a*t**2
print(s)

a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print ('First equation: %g = %g' % (eq1_sum, eq1_pow))
print ('Second equation: %g = %g' % (eq2_sum, eq2_pow))