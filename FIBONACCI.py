# -*- coding: utf-8 -*-
"""
@author: Belanda
"""




def fib(n: int) -> int: 
   if n == 0: return 0 
   value1, value2 = 1, 1 
   while n > 2: 
      value1, value2 = value2, value1+value2 
      n -= 1 
      
   print(value2)
   
 

fib(10)