import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Longitud de la contraseña: "))
contrasena_generada = ""

for i in range(longitud):
    contrasena_generada = contrasena_generada + random.choice(characters)


print(contrasena_generada)