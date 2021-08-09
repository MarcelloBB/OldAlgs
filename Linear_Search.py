# -*- coding: utf-8 -*-
"""
// Marcello 
"""

def procura(lista, elemento):
    assert isinstance(lista, list)
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return indice
    else:
        return None
    
print(procura([1, 2, 3], 2))
