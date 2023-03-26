import math

# Pedimos al usuario que ingrese el capital inicial
capital = float(input("Ingrese el capital inicial: "))

# Calculamos el monto al que se duplica el capital inicial
monto_duplicado = capital * 2

# Definimos la tasa de interés y la cantidad de meses
tasa_interes = 0.05
meses = 0

# Mientras el capital no se haya duplicado, seguimos acumulando intereses
while capital < monto_duplicado:
    capital *= 1 + tasa_interes
    meses += 1

# Imprimimos el resultado
print("El capital se duplica en", meses, "meses")
