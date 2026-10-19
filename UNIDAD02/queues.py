from collections import deque
import time
cola_reproduccion=deque()
cola_reproduccion.append("1.tiburon")
cola_reproduccion.append("2.historia de amor")
cola_reproduction.append("3.historia entre tus dedos")
#MOSTRAR LAS CANCIN EN ESPERA
print("canciones en espera: ")
for cancion in cola_reproduccion:
    print("__",cacion)
    print("iniciando reproduccion")
#el reproductor procesa la cola cancion por cancion(fsedkfnñwef)
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora{cancion_actual}")
    time.sleep(1) #simula la duracion del tema
    print(f"finalizo: {cancion_actual}")
#muestra cuantas canciones le quedan en la cola
int(f"quedan {len(cola_reproduccion)})canciones en la cola)")
int("la cola de reproduccion ha terminado.")
