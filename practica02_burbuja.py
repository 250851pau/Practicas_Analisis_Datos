lista = [85,70,95,60,88,72,100,76,91,65,83,78,94,69,87]

# Orden ascendente
ascendiente = lista.copy()

swapped = True

while swapped:
    swapped = False

    for i in range(len(ascendiente)-1):
        if ascendiente[i] > ascendiente[i+1]:
            ascendiente[i], ascendiente[i+1] = ascendiente[i+1], ascendiente[i]
            swapped = True

print("Orden ascendente:", ascendiente)


# Orden descendente
descendiente = lista.copy()

swapped = True

while swapped:
    swapped = False

    for i in range(len(descendiente)-1):
        if descendiente[i] < descendiente[i+1]:
            descendiente[i], descendiente[i+1] = descendiente[i+1], descendiente[i]
            swapped = True

print("Orden descendente:", descendiente)
