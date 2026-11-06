#def factorial_iterativo(n):
#    resultado=1
#    for i range(1,n+1):
#        resultado=resutlado*i 
#    return resultado
#print(factorial_iterativo(5))


#def factorial (n):
#    if n==0:
#        return 1
#    else:
#        return n*factorial(n-1)
#print(factorial(5))

def potencia(base, exponente):
    if exponente==0:
        return 1
    else: 
        return base*potencia(base, exponente -1)
print(potencia(2,4))


def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # 1. Mover n-1 discos de 'origen' a 'auxiliar'
    hanoi(n - 1, origen, auxiliar, destino)
    
    # 2. Mover el disco más grande restante al 'destino'
    print(f"Mover disco {n} de {origen} a {destino}")
    
    # 3. Mover los n-1 discos de 'auxiliar' a 'destino'
    hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso con 3 discos
hanoi(3, 'A', 'C', 'B')