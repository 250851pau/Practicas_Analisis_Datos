historial_navegacion=[]
#operacion para apilar(push)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.com")
print("historial cargado", historial_navegacion)

#operacion cima (top-peek)
pagina_actual=historial_navegacion[-1]
print("pagina actual en pantalla",pagina_actual)

#peracion para desapilar(pop)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de:" , pagina_cerrada)
print("historial despues de presionar atras", historial_navegacion)

#operacion tamaño
total_paginas=len(historial_navegacion)
print("paginas guardadas", total_paginas)

#operacion vacia(empty)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio", sin_paginas)


