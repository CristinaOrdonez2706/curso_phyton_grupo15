#Programa para para validación de númeor par e impar.

try:
    numero = input("Ingresa un número: ")
    numero = int(numero)
    
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")
except ValueError:
    print("Error: Ingresa un número válido.")
