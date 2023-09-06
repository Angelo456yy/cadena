#el usuario escribe su correo
correoelec = input("escribe tu correo electronico un ejemplo ***********@gmail.com : ")

correoel = correoelec.split('@')[0]
correomod = correoel + "@ceu.es"
#el usuario recibe su correo modificado
print(correomod)