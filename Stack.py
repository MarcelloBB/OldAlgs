# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""


#Stacks


stack = []

stack_size = 3

def showStack():
    print('Stack currently contains: ')
    for item in stack:
        print(item)
        
    
def add(value):
    if len(stack) < stack_size:
        stack.append(value)
        
    else:
        print('stack is full')
        
        
def pop():
    if len(stack) > 0:
        print('Popping: ', stack.pop())
        
    else:
        print('stack is empty')
        
        
add(3)
add(4)
showStack()
pop()