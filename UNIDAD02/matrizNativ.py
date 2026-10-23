#CREACIÓN DE MATRIZ DE 3X3
matriz= [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
#ACCESO A ELEMENTOS MATRIZ(FILA)(COLUMNA)
print(matriz[1][2])#imprimiria fila indice 
#MODIFICAR LA MATRIZ    
matriz[0][0]=100
#RECORRER MATRIZ
for fila in matriz:
    for elemento in fila:
          print(elemento, end=" ")
    print()



#A=[[1,2],[3,4]]
#B=[[5,6],[7,8]]
#suma=[[A[i][j]+B[i][j] for j in range (len(A[0]))] for i in range(len(A))]
#print(suma) 