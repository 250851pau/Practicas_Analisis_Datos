import numpy as np


#MANERA 1
# MATRIZ A Y B
Sucursal_A = np.array([[10, 15], [20, 5]])
Sucursal_B = np.array([[5, 12], [15, 8]])

print("ventas del sabado")
print(Sucursal_A)
print("ventas del domingo")
print(Sucursal_B)

#cantidad de productos vendidos
print("cantidad de productos vendidos: ")
total_productos_np =Sucursal_A + Sucursal_B
print(total_productos_np)

#ingreso total
precio=50
ingreso_total_np=total_productos_np*precio
print("ingreso total: ")
print(ingreso_total_np)



print("######################################################")
#MANERA 2
matriz1= [
    [10,15],
    [20,5]
]
matriz2= [
    [5,12],
    [15,8]
]
print("ventas del sabado")
print(matriz1)
print("ventas del domingo")
print(matriz2)

total_productos=[]

for i in range(len(matriz1)):
    fila=[]
    for j in range(len(matriz1[0])):
        fila.append(matriz1[i][j]+matriz2[i][j])
    total_productos.append(fila)

precio=50
ingreso_total=[]
for i in range(len(total_productos)):
    fila=[]
    for j in range(len(total_productos[0])):
        fila.append(total_productos[i][j]*precio)
        ingreso_total.append(fila)

print("total de productos vendidos: ")
for fila in total_productos:
    print(fila)
    
print("ingreso total: ")
for fila in ingreso_total:
    print(fila)





