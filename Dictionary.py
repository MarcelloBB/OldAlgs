# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""

colors = {'Sam':'Blue', 'Amy':'Red', 'Sarah':'Yellow'}

#searching
print(colors['Sarah'])

# keys
print(colors.keys())


for i in colors.keys():
    print()
    print(f'{i} likes the color {colors[i]}')

#update ==>   
colors.update({'Harry':'Orange'})
colors.update({'Sam':'Purple'})

del colors['Sam']

print(colors)