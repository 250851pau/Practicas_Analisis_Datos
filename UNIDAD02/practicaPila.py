
historial_libros = []

# OPERACION PARA APILAR (PUSH)
historial_libros.append("Matematicas")
historial_libros.append("Español")
historial_libros.append("Ciencias")

print("Pila cargada:", historial_libros)

# OPERACION CIMA (TOP-PEEK)
libro_actual = historial_libros[-1]
print("Libro en la cima:", libro_actual)

# OPERACION PARA DESAPILAR (POP)
libro_retirado = historial_libros.pop()
print("Libro retirado:", libro_retirado)
print("Pila despues de retirar:", historial_libros)

# OPERACION TAMAÑO
total_libros = len(historial_libros)
print("Libros guardados:", total_libros)

# OPERACION VACIA (EMPTY)
sin_libros = len(historial_libros) == 0
print("¿La pila esta vacia?", sin_libros)

# CICLO WHILE PARA RETIRAR TODOS LOS ELEMENTOS
while len(historial_libros) > 0:
    libro_retirado = historial_libros.pop()
    print("Libro retirado:", libro_retirado)
    print("Pila actual:", historial_libros)

# COMPROBAR SI LA PILA ESTA VACIA
sin_libros = len(historial_libros) == 0
print("¿La pila esta vacia al final?", sin_libros)