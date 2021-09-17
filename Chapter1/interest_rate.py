# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:53:08 2021

@author: hp
"""

A = 1000
p = 5
n = 3
money = A*(1+ (p/100))**n
print("""
      After %d years, initial amount of %.1f euros
      with inrerest rate of %.1f will become %.2f
      """%(n,A,p,money))