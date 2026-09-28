#solo se admiten personas con mayoria de edad
#con argumento
#1-.
def admitir_edad(nombre,edad):
    print(f"tu nombre es: {nombre}, tienes {edad} años.")

    if edad >18:
        print(f"tu edad cumple con el rango de edad permitido, puede pasar. ")
    else:
        print("No tienes permitido pasar,  ¿donde estan tus padresss?? ")

admitir_edad("Pillo",15)

#2-.
def calcular_descuento(precio,porcentajeDescuento):
    print(f"el precio inicial es de: {precio}, el descuento que se le va a hacer al producto es de: {porcentajeDescuento}")
    total=precio -(precio*porcentajeDescuento)
    return total
precioFinal=calcular_descuento(100,0.20)
print(f"El precio del producto con descuento es: {precioFinal}")


#sin argumento
#1-.
def admitir_edad():
    nombre = "Pillo"
    edad = 19
    
    print(f"Tu nombre es: {nombre}, tienes {edad} años.")
    if edad >= 18: 
        print("Tu edad cumple con el rango de edad permitido, puede pasar.")
    else:
        print("No tienes permitido pasar, ¿dónde están tus padres?")

admitir_edad()

#2-.
precio_original = 100
descuento = 20  

dinero_descontado = precio_original * 0.20

precio_final = precio_original * (1 - (descuento / 100))

print(f"precio inicial del producto: ${precio_original}")
print(f"Te descuentan: ${dinero_descontado}")
print(f"Precio final a pagar: ${precio_final}")