saldo = 1000
n_de_operaciones = int(input("por favor ingrese cuantas operaciones quiere realizar: "))

for i in range(n_de_operaciones):
    print ("1 → Consultar saldo")
    print ("2 → Retirar dinero")
    print ("3 → Depositar dinero")
    opcion = input("por favor ingrese la opcion: ")

    if opcion == "1":
        print("su saldo es", saldo)
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

    if opcion == "3":
        #opcion 3
        monto = float(input("ingrese el monto que desea depositar: "))
        while monto < 0:
            monto = float(input("ingrese una cantidad valida, vuelva intentar"))
        
        if monto > 0:
            saldo += monto
            print(f"usted ingreso con exito {saldo} a su cuenta")
    if opcion not in ["1", "2", "3"]:
        print("opcion no valida, vuelva a intentar")    
    
        

# finalizacion del cajero:
print("\nGracicas por usar el cajero automatico.")   


