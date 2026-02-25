print ("Hola mundo")
def cajero_automatico():
    saldo = 1000
    print("Bienvenido al cajero automático")
    print(f"Su saldo inicial es: ${saldo}")

    while True:
        try:
            operaciones = int(input("¿Cuántas operaciones desea realizar? "))
            if operaciones > 0:
                break
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    for i in range(operaciones):
        print("Operación", i + 1)
        print("Menú:")
        print("1 -> Consultar saldo")
        print("2 -> Retirar dinero")
        print("3 -> Depositar dinero")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción inválida")
            continue

        if opcion == 1:
            print(f"Su saldo actual es: ${saldo}")

        elif opcion == 2:
            while True:
                try:
                    monto = float(input("Ingrese el monto a retirar: "))
                    if monto < 0:
                        print("El monto no puede ser negativo. Intente nuevamente.")
                    elif monto > saldo:
                        print("Fondos insuficientes.")
                        break
                    else:
                        saldo -= monto
                        print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                        break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

        elif opcion == 3:
            while True:
                try:
                    monto = float(input("Ingrese el monto a depositar: "))
                    if monto < 0:
                        print("El monto no puede ser negativo. Intente nuevamente.")
                    else:
                        saldo += monto
                        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
                        break
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

        else:
            print("Opción inválida")

    print("Gracias por usar el cajero automático")
    
    
cajero_automatico()