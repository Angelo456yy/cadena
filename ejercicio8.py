#que el usuario escriba el precio del producto
precio = float(input("Escriba el precio del producto con decimales: "))


euros, centimos = divmod(int(precio * 100), 100)

#lo que recibe es el euro y los sentimos por aparte
print("Solo euros:", euros)
print("Solo céntimos:", centimos)