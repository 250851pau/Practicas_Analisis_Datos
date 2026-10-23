import datetime
def saludar():
    print("Hola, bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().striftime("%H","%M","%S")
    print(f"La hora actual es: {hora_actual}")
mostrar_hora()

#Now()consulta el reloj o la hora de SO
#Strftime convertir la fecha y hora en texto, usando el formato establecido
#f-string la letra f indica a python que procese el texto
#e inserte las variables dentro e las llaves
#{hora_actual} se toma el valor almacenado en la variable de hora_actual
#y lo reeemplaza ahi mismo