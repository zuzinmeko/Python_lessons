# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:46:39 2021

@author: hp
"""

meters = 640
inches = meters*100/2.54
feet = inches/12
yards = feet/3
miles = yards/1760
print("""
%d meter is equal to
%.2f inches,
%.2f feet,
%.2f yards and
%.2f miles      
"""%(meters, inches, feet, yards, miles))