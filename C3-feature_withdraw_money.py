#Jesus Hernandez #Kevin Pino #Sebastian Arevalo
if opcion == "2":
        #opcion 2
        retirar = int(input("por favor ingrese cuanto desea retirar: "))
        while retirar < 0:
            retirar = float(input("es un numero negativo, ingresa una cantidad valida"))
        
        if retirar > saldo:
            print("monto insuficiente")
        elif retirar <= saldo: 
            saldo -= retirar
            print (f"saldo actual: {saldo} ")