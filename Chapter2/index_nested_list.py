# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:37:20 2021

@author: Lenovo
"""

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
print (q[0][0])
print (q[1]) #list (d,e,f)
print (q[-1][-1]) #last element 'h'
print (q[1][0]) #letter 'd'

for i in q: #i are the lists of elements within q
    for j in range(len(i)): #j are the letters within the list
        print (i[j])