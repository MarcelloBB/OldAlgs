# -*- coding: utf-8 -*-
"""
// @author: Marcello Belanda
"""


#####################################################################################
print()

def factorial_i(n):
    
    resultado = 1
    
    while n > 1:
        print('Factorial with n == ', n)
        resultado *= n
        n -= 1
         
        
        if n < 1:
            print('End')
            return 1
        
        elif n == 1:
            
            print('Factorial with n ==  1')
            print()
            
            return resultado

print('The result is: ', factorial_i(3))
