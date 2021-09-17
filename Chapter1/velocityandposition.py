# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:37:38 2021

@author: hp
"""

v0 = 3
g = 9.81
t = 0.6
position = v0*t - 0.5*g*t*t
velocity = v0 - g*t
print ('position: ',position,'velocity: ',velocity)
