def change():
    expense = 23.75
    money = 100

    a = money - expense
    a = int(a)

    b = money - expense
    c = b - a 
    d = c * 100 
    d = int(d)

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(a)
    print("Centavos:")
    print(d)

change()