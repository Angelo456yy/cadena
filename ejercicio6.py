#la vocal sera estara en mayuscula 
palabra = input("escriba una palabra random: ")

vocal = input("escriba una vocal: ")

palabra_1 = palabra.replace(vocal, vocal.upper())

print(palabra_1)