# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""


#queues 
# FIFO, First In First Out

#------------------------------------------------------------------------------
import queue 
#------------------------------------------------------------------------------

my_queue = queue.Queue(3)


print('Queue empty: ', my_queue.empty())


my_queue.put(1)
my_queue.put(2)
my_queue.put(3)


print('Queue full: ', my_queue.full())


print('Popping: ', my_queue.get())
print('Queue full: ', my_queue.full())


print('Popping: ', my_queue.get())
print('Popping: ', my_queue.get())


print('Queue empty: ', my_queue.empty())