# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:07:51 2021

@author: hp
"""

v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)

t = 0.6; y = 1.2342
print('At t=%g s, y is %.2f m.' %(t, y))

initial_velocity = 5
accel_of_gravity = 9.81
TIME = 0.6
VerticalPositionOnBall = initial_velocity*TIME - \
    0.5*accel_of_gravity*TIME**2
print(VerticalPositionOnBall)