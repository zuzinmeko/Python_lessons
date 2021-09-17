# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 10:02:24 2021

@author: hp
"""
while True:
    data = eval(input("Enter input data(None to quit) :"))
    if data is not None:
        print("You've entered %s  data with the value %s."%(type(data),data))
    