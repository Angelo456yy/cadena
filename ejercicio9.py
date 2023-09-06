#el usuario debe escribir su fecha
fecha = input("escriba su fecha de nacimiento \n De la siguiente forma dd/mm/aaaa: ")

partes = fecha.split('/')

if len(partes) == 3:
    dia = partes[0]
    mes = partes[1]
    años = partes[2]

#la fecha es separa por dia,mes y año
    print("Día:", dia)
    print("Mes:", mes)
    print("Año:", años)