saldo = 1000
print("hola")

def retirar_dinero(cantidad):
    global saldo
    if cantidad > saldo:
        print("No tienes suficiente dinero")
    else:
        saldo -= cantidad
        print("Has retirado", cantidad, "tu nuevo saldo es", saldo)