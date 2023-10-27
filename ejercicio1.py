#Programa para para validación de númeor par e impar.

numero = int(input("Ingrese un número: "))


if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
