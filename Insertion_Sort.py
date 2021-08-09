# -*- coding: utf-8 -*-
"""
// Marcello Belanda
"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3, 11, 15, 12, 14, 13, 20, 21, 42, 23, 45]

print()
print('Original data:')
print(data)
print('_'*90)


for scanIndex in range(1, len(data)):
    temp = data[scanIndex]
    
    minIndex = scanIndex
    
    while minIndex > 0 and temp < data[minIndex - 1]:
        data[minIndex] = data[minIndex - 1]
        
        minIndex -= 1
        
    data[minIndex] = temp
    
    print(data)
    
print('_'*90)
print('Organized Data:')
print(data)



#--------------------------------------------------------------------------
print()

def insertion_sort(lista):
  for i in range(1, len(lista)):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave
    print(lista) 

lista = [1, 4, 5, 6, 3, 2, 100, 72, 939, 83, 13, 33,]
insertion_sort(lista)

