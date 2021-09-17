# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:40:42 2021

@author: hp
"""

infile = open('fdeg.dat','r')
for i in range(3):
    infile.readline()
lines = infile.readline()
infile.close()

words = []
Fdegrees = []
Cdegrees = []
for line in range(len(lines)):
    words = lines.split()
    Fdegrees.append[words[2]]
    Cdegrees.append(5/9*(float(words[2])-32))
outfile = open('Degrees.dat','w')
for i in range(len(Cdegrees)):
    row = (Fdegrees[i],Cdegrees[i])
    outfile.writelines(str(row))
outfile.close()
