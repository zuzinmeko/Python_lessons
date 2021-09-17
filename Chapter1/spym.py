# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:28:08 2021

@author: hp
"""

from sympy import *  
t, v0, g = symbols('t v0 g')
y = v0*t - rational(1,2)*g*t**2
dypt = diff(y, t)
print(dypt)
print('acceleration: ', diff(y, t, t))
print(integrate(dydt, t))