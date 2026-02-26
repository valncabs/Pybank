    elif opcion == "3":
        #opcion 3
        monto = float(input("ingrese el monto que desea depositar: "))
        while monto < 0:
            monto = float(input("ingrese una cantidad valida, vuelva intentar: "))
        
        if monto > 0:
            saldo += monto
            print(f"usted ingreso con exito {saldo} a su cuenta")
    
    else:
        #validacion de las opciones
        print ("opcion invalida")
        
        
# finalizacion del cajero:
print("\nGracicas por usar el cajero automatico.")