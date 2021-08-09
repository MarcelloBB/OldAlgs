# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

print()
print('Original Data:')
print(data)
print('_'*90)

for i in range(0, len(data)):
    k = i
    
    for c in range(i + 1, len(data)):
        if data[c] < data[k]:
            k = c
            
    if k != i:
        data[i], data[k] = data[k], data[i]
        print(data)

print('_'*90)        
print('Organized Data:')
print(data)

    

