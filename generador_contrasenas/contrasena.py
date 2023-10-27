import random

class GeneradorContrasena:
    def generar_contrasena(self, minuscula, mayuscula, numerico, longitud):
        abecedario = "abcdefghijklmnopqrstuvwxyz"
        contrasena = []

        for _ in range(minuscula):
            contrasena.append(random.choice(abecedario))

        abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for _ in range(mayuscula):
            contrasena.append(random.choice(abecedario))

        for _ in range(numerico):
            contrasena.append(str(random.randint(0, 9)))

        random.shuffle(contrasena)

        return "".join(contrasena)
