import numpy as np

a = np.array([ [1, 2, 3, 4, 5],
               [10, 20, 30, 40, 50],
               [100, 200, 300, 400, 500] ])

print(a)
print('-----------------------------')

print(a.ndim)
print('-----------------------------')

print(a.shape)
print('-----------------------------')

print(a.size)
print('-----------------------------')

print(a[0][0])
print('-----------------------------')

print(a[2][4])
print('-----------------------------')

# mejor practica
print(a[2, 4])
print('-----------------------------')

print(a[1][1:4])
print('-----------------------------')

print(a[1, 1:4])
print('-----------------------------')

print(a[1, [0, 2, 3]])
print('-----------------------------')

a.ravel() # Una vista

print(a)
print('-----------------------------')

a.flatten() # Una copia

print(a)
print('-----------------------------')

