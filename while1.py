# Bucle white
import math

numero = int(input("Digite un numero: " ))

while numero<0:
    print("error -> deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")



