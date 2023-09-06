#escriibir su numero de telefono 
telefono = input("Escriba su numero de telefono como en este ejemplo +34-xxxxxxxxx-xx: ")

#con esto eliminaremos los dijitos
numero = telefono.split('-')[1]

#el numero de telefono sin su region
print("Su numero de telefono  es:", numero)