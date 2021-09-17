# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:32:54 2021

@author: hp
"""
infile = open('data.txt','r')
for i in range(3):
    infile.readline()
line = infile.readline()
infile.close()
words = []
words = line.split()
F = float(words[2])
C = 5/9*(F-32)
print("Celsius degree: ",C)