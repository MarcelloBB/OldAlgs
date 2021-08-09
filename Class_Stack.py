# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""
#The Stack 



class Stack: 
    global stack, stack_size
    
    def __init__(self, stack, stack_size):
        self.stack = stack
        self.stack_size = stack_size
    
    def showStack(self):
        print('Stack currently contains: ')
        c = 0
        for item in self.stack:
            print(c, '-', item)
            c += 1
         
        print()
        
    def addItem(self, value):
        if len(self.stack) < self.stack_size:
            self.stack.append(value)
            print(f'Value: {value} added')
        else:
            print()
            print(f'Stack is full! {value} is out')
    
    def pop(self):
        if len(self.stack) > 0:
            print(f'Popping the last element : {self.stack.pop()}')
            
        else:
            print('Stack is empty')
              
        
s = Stack([], 5)

# tests I
print()
print('_'*90)
print('Stack ARGS')
print('_'*90)
print('stack.stack = ', s.stack)
print('stack.stack_size = ', s.stack_size)



# tests II
print()
print('_'*90)
print('Stack Funcs')
print('_'*90)
s.addItem(5)
s.addItem(10)
s.addItem(100)
s.addItem(13)
s.addItem(223)
s.addItem(189) #stack is full
print()
s.showStack()
s.pop()