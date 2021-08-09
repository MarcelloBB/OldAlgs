# -*- coding: utf-8 -*-
"""
// @ MARCELLO

"""

# // + --------------
# // + BINARY SEARCH
# // + --------------

print()

def search(searchList, key):
    
    #hanf ->
    mid = int(len(searchList) / 2)
    
    #searching midpoint ->
    print('Searching midpoint at ', str(searchList[mid]))
    print()
    
    if mid == 0:
        print('Key not found !')
        return key
    
    elif key == searchList[mid]:
        print('Key found!')
        print()
        return searchList[mid]
    
    elif key > searchList[mid]:
        print('SearchList now contains ', searchList[mid:len(searchList)])
        print()
        search(searchList[mid:len(searchList)], key)
        
    else:
        print('searchList now contains ', searchList[0:mid])
        print()
        search(searchList[0:mid], key)
    
# database -> 
aList = list(range(10,1000))

#  running / n=109
search(aList, 109)