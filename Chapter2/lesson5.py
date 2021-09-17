# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:52:19 2021

@author: hp
"""

s = 0
k = 1
M = 100
while k < M:
    s += 1/k
    k += 1
print(s)

s = 0
k = 1
M = 100
while k <= M:
    s += 1.0/k
    k += 1
print(s)