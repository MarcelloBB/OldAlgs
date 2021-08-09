# -*- coding: utf-8 -*-
"""
// marcello belanda
"""

#graphs

#all conections
graph = {'A': ['B', 'F'],
         'B': ['A', 'C'],
         'C': ['B', 'D'],
         'D': ['C', 'E'],
         'E': ['D', 'F'],
         'F': ['A', 'E']}


def find_path(graph, start, end, path = []):
    path = path + [start] #path = ['B']
    
    if start == end:
        print('ending...')
        return path
    
    for node in graph[start]: #['B']
        print('Checking node ', node)
        
        if node not in path:
            print('path so far ', path)
            newp = find_path(graph, node, end, path)
            if newp:
                return newp
            

find_path(graph, 'B', 'E')
            