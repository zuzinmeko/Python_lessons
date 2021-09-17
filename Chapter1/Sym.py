# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:28:08 2021

@author: hp
"""

from sympy import *  
t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1,2)*g*t**2
dydt = diff(y, t)
print(dydt)
print('acceleration: ', diff(y, t, t))
print(integrate(dydt, t))