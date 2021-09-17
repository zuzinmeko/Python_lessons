# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:59:59 2021

@author: hp
"""

#initilize values
g = 9.81
v0 = 15
theta = 60
x = 0.5
y0 = 1
print("""v0 = %.1f km/h
theta = %d degrees
y0 = %.1f m
x = %.1f m""" % (v0, theta, y0, x))

v0 = v0/3.6
from math import pi, tan, cos
theta = theta*pi/180
y = x*tan(theta) - 1/(2*v0)*g*x**2/((cos(theta))**2) + y0
print('y = %.1f m' % y)