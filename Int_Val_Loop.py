# -*- coding: utf-8 -*-
"""
// @author: Belanda
"""

n_truth = True

while n_truth:
    try:
        n = int(input('Enter INT: '))
        n_truth = False
        
    except ValueError:
        print('error')
        


