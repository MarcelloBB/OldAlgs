# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:36:06 2021

@author: user
"""


#########################################################################
#The recursion uses a function until its false

#Recursion factorial version
print()

def factorial_r(n):
    print('Factorial with n == ', n)
    if n == 1 or n == 0:
        print()
        print('End')
        print()
        return 1
    else:
        return n * factorial_r(n-1)

print('The result is: ', factorial_r(5))
print('_'*92)