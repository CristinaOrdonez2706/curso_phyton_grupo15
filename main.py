from generador_contrasenas.contrasena import GeneradorContrasena

print("**GENERADOR DE CONTRASEÑAS****")

minuscula = int(input("Indique número mínimo de minúsculas: "))
mayuscula = int(input("Indique número mínimo de mayúsculas: "))
numerico = int(input("Indique número mínimo de caracteres numéricos: "))
longitud = int(input("Indique longitud de la contraseña: "))

generador = GeneradorContrasena()
contrasena_generada = generador.generar_contrasena(minuscula, mayuscula, numerico, longitud)

print(f"SU CONTRASEÑA ES: {contrasena_generada}")
