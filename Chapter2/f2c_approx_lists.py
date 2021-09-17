# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:45:15 2021

@author: Lenovo
"""

print ('--------------------')
Fn = 0
dF = 10
F = []; C=[]; C2=[]
print ('%5s %8s %8s'% ('F', 'C', 'C2'))
while Fn <= 100:
    Cn = 5.0/9 * (Fn-32)
    Cn2 = (Fn-30)/2.0
    F.append(Fn), C.append(Cn), C2.append(Cn2)
    Fn = Fn + dF
conversion = [[F[i], C[i], C2[i]] for i in range(len(F))]
for i in range(len(conversion)):
    print ('%5d %8.4f %8.4f' % (conversion[i][0], conversion[i][1], conversion[i][2]))
print ('--------------------')