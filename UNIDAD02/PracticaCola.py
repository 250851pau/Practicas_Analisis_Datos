from collections import deque

# CREAR UNA COLA
cola = deque()

# AGREGAR PERSONAS (ENCOLAR)
cola.append("Samuel")
cola.append("Maria")
cola.append("Pedro")

# MOSTRAR LA COLA INICIAL
print("Personas en espera:", cola)

# ATENDER A LA PRIMERA PERSONA (DESENCOLAR)
atendido = cola.popleft()

# MOSTRAR RESULTADOS
print("Persona atendida:", atendido)
print("Personas restantes:", cola)