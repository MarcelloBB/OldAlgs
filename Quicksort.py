# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def partition(data, left, right):
    pivot = data[left]
    leftIndex = left + 1
    rightIndex = right
    
    while True:
        while leftIndex <= rightIndex and data[leftIndex] <= pivot:
            leftIndex += 1
            
        while rightIndex >= leftIndex and data[rightIndex] >= pivot:
            rightIndex -= 1
            
        if rightIndex < leftIndex:
            break
        data[leftIndex], data[rightIndex] = data[rightIndex], data[leftIndex]
        print(data)
        
    data[left], data[rightIndex] = data[rightIndex], data[left]
    print(data)
    return rightIndex


def quicksort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data, left, right)
        quicksort(data, left, pivot - 1)
        quicksort(data, pivot + 1, right)
    return data
quicksort(data, 0, len(data) - 1)

#----------------------------------------------------------------
def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):

    # para uma versão com partição aleatória
    # descomente as próximas três linhas:
    # from random import randrange
    # rand = randrange(ini, fim)
    # a[rand], a[fim - 1] = a[fim - 1], a[rand]
    
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1
print()

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
print(a)
print(quick_sort(a))
        

