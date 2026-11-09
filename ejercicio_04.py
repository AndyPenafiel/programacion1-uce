n = int(input("Ingrese un número entero positivo: "))

if n > 0:
    suma = 0
    for i in range(1, n + 1):
        suma = suma + i
    print("La suma del 1 hasta", n, "es:", suma)

else:
    print("Error: El número debe ser positivo.")