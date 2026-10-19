#<gestionar una lista de nombres de estudiantes mediante operaciones de insercion,
#busqueda por indice y extraccion de sublistas.>
#1. crear una lista llamada estudiantes que contenga tres nombres: ana, carlos y diana {}
#2. imprimir la lista original{}
#3. agregar al final de la lista a elena con metodo insert{}
#4. agregar a beatriz en la posicion con indice 1 utilizando el metodo insert{}
#5. mostrar la lista actualizada{}
#6. imprimir el primer elemento de la lista{}
#7. metodo index para encontrar la posicion numerica exacta en la que se
#encuentra diana e imprimir{}
#8. mostrar los primeros 3 estudiantes de la lista con slicing e imprimirlos{}
#9.  extraer subgrupo con los elementos que van desde el indice 1 hasta el 3 y mostrarlo{}
#10. obtener los ultimos 2 estudiantes utilizando numeros negativos{}
#11. crear una nueva lista con el orden inverso utilizando un paso negativo y mostrarla{}



#1-. <--------------CREACION DE LA LISTA INICIAL------------------------>
estudiantes = ["ana","carlos","diana"]
print("1. la lista de estudiantes es la siguiente: ")
print(estudiantes[::])
print("2. se agrego al estudiante elena al final de la lista")
estudiantes.append("elena")
print(estudiantes[::])
print("3. se agrego al estudiante beatriz en la posicion 1")
estudiantes.insert(1,"beatriz")
print(estudiantes[::])
print("4. el primer estudiante de la lista es: ")
print(estudiantes[0])
print("5. el estudiante en el indice 2 es:")
print(estudiantes[2])
print("6. la posicion de diana en la lista es: ")
print(estudiantes.index("diana"))
print("7. los primeros 3 estudiantes de la lista son: ")
print(estudiantes[0:3])
subgrupo = estudiantes[1:4]
print("8. el subgrupo de estudiantes es: ")    
print(subgrupo)
ultimos = estudiantes[-2:]
print("9. los ultimos 2 estudiantes de la lista son: ")
print(ultimos)
print("10. la lista de estudiantes en orden inverso es: ")
print(estudiantes[::-1])