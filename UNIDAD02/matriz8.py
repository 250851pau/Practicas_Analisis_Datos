import numpy as np

# MATRIZ A Y B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# SUMA DE ELEMENTOS
suma = A + B
print("--SUMA (A+B)--")
print(suma)

# MULTIPLICACIÓN ELEMENTO A ELEMENTO
prod_elem = A * B
print("--MULTIPLICACIÓN ELEMENTO A ELEMENTO (A*B)--")
print(prod_elem)

# PRODUCTO MATRICIAL
prod_mat = A @ B
print("--PRODUCTO MATRICIAL (A@B)--")
print(prod_mat)

# TRANSPUESTA
transpuesta = A.T
print("--TRANSPUESTA DE A (A.T)--")
print(transpuesta)

# DETERMINANTE E INVERSA
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)

print("--DETERMINANTE DE A--")
print(det_A)

print("--INVERSA DE A--")
print(inv_A)

