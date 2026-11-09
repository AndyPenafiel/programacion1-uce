saldo = 500

while True:
    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Su saldo actual es: $", saldo)

    elif opcion == 2:
        deposito = float(input("Ingrese el valor a depositar: "))

        if deposito > 0:
            saldo = saldo + deposito
            print("Depósito realizado correctamente.")
        else:
            print("El depósito debe ser mayor a cero.")

    elif opcion == 3:
        retiro = float(input("Ingrese el valor a retirar: "))

        if retiro > 0 and retiro <= saldo:
            saldo = saldo - retiro
            print("Retiro realizado correctamente.")
        else:
            print("Valor inválido o saldo insuficiente.")

    elif opcion == 4:
        print("Gracias por utilizar nuestro cajero.")
        break

    else:
        print("Opción no válida.")