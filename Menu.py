#codigo saldo incial del usuario

n_de_operaciones = int(input("por favor ingrese cuantas operaciones quiere realizar: "))

#menu
for i in range(n_de_operaciones):
    print ("1 → Consultar saldo")
    print ("2 → Retirar dinero")
    print ("3 → Depositar dinero")
    opcion = input("por favor ingrese la opcion: ")
