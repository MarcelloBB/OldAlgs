# -*- coding: utf-8 -*-
"""
// MARCELLO BELANDA
"""

# MODULES
import numpy as np
from itertools import permutations
from itertools import combinations
from random import sample


a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 3, 5])

print(a==b)

print()

# BOOL ARRAY
x = np.array([True, False, True, False])
y = np.array([True, True, False, False])

# LOG OR
print(np.logical_or(x, y), 'ou')

# LOG AND
print(np.logical_and(x, y), 'e')

# LOG NOT
print(np.logical_not(x), 'não x')
print(np.logical_not(y), 'não y')

# LOG XOR
print(np.logical_xor(x, y), 'xor')

print(f'{x * y}=> x * y')
print(f'{x + y}=> x + y')

print(f"{a + b}=>a+b")
print(f"{a - b}=>a-b")
print(f"{a * b}=>a*b")
print(f"{a / b}=>a/b")

print()

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz)

matrix_index = matriz[0, 0] # linha, coluna
print(matrix_index)

print('_'*92)

# QUAD 
matriz_q = np.array([[[[[1, 2, 3], [4, 5, 6]]]]])
print(matriz_q, '====> Matriz Quadridimensional')

print('_'*92)

# ONE_MATRIX => SHAPE[4,4]
oneMatrix = np.ones([4, 4])
print(oneMatrix, '====> Matriz Ones')

print('_'*92)

# ZERO_MATRIX => SHAPE[4,4]
zeroMatrix = np.zeros([4, 4])
print(zeroMatrix, '====> Matriz Zeros')

print('_'*92)

#---------------------------------------------------

# TRUE
TrueMatrix = np.ones([4, 4], dtype=np.bool)
print(TrueMatrix, '====> Matriz dtype=True(1)')

print('_'*92)

# FALSE 
FalseMatrix = np.zeros([4, 4], dtype=np.bool)
print(FalseMatrix, '====> Matriz dtype=False(0)')

print('_'*92)

# INV
a = np.array([[1, 2], [3, 4]])
inverso_a = np.linalg.inv(a)
print(a, '====> Matriz Comum')
print('_'*92)
print(b, '====> Matriz Inversa')

print('_'*92)

# IDENT
print(np.identity(5), '====> Matriz Identidade')
print('_'*92)

#-----------------------PERMUTAÇÕES-----------------------------
array = np.array([1, 2, 3, 4])
print(array, '====> Matriz Normal')
print('_'*92)

# PERMUTATION
print(np.random.permutation(array), '====> Matriz Permutada (np.random.permutation)')
print('_'*92)

matriz = np.array([1, 2, 3])

for permutation in permutations(matriz):
    print('Permutation: ', permutation)
    
print('_'*92)

permutations_list = list()
for permutation in permutations(matriz):
    permutations_list.append(permutation)
    print(permutation, 'Added')
    
print('All the permutations: ', permutations_list)

print('_'*92)

#-----------------------------COMBINAÇÕES----------------------

for comb in combinations(matriz, 2): 
    print(comb)
    
print('_'*92)

#--------------------------------------------------------------

pool = [comb for comb in combinations(matriz,2)]     

print(sample(pool, 3))

print('_'*92)

#--------------------------------REPETIÇÕES------------------------------
a = np.array([1, 2, 3, 4, 5, 7, 7, 7, 1, 10]) 

b = np.array(list(set(a))) 

cb = np.array(set(a)) 


print(f'Array (a) => {a}')
print('_'*92)
print(f'Array (b) SEM list()=> {cb}')
print('_'*90)
print(f'Array (b) COM list()=> {b}')