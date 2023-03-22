#While

#x = 0
#while x < 10:
#    print("el valor de x es:",x)
#    x += 1

#num = int(input("Escribe un numero positivo"))
#while num < 0:
#    print("Este es un numero negativo, prueba de nuevo")
#    num = int(input("Escribe un numero positivo"))
#print ("el numero es: ", num)

#ejemplo de un menu

num = int(input("Menu: 1(ver numeros), 0(salir) "))
while num != 0:

    x = 0 
    while x < 10:
        print("El valor de x es: ",x)
        x += 1
        
        print("Saliendo,,,")
        num = int(input("Menu: 1(ver numeros), 0(salir)"))
print("Gracias")
