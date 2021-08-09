# -*- coding: utf-8 -*-
"""
# // @Marcello
"""

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