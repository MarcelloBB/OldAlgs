# -*- coding: utf-8 -*-
"""
// Marcello Belanda
"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def merge(left, right):
    
    if not len(left):
        return left
    
    if not len(right):
        return right
    
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left)  + len(right)
    

    while len(result) < totalLen:
 
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            
            leftIndex += 1
        
        else:
            result.append(right[rightIndex])
            
            rightIndex += 1
        
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
        
    return result
        

    
def mergesort(list_a):
    if len(list_a) < 2:
        return list_a
    

    middle = len(list_a) // 2 #11 // 2 = 5

    left = mergesort(list_a[:middle])
    right = mergesort(list_a[middle:])
    
    print()
    print('Left side: ', left)
    print('Right side: ', right)
    
    merged = merge(left, right)
    
    print('Merged: ', merged)
    
    return merged
    

mergesort(data)