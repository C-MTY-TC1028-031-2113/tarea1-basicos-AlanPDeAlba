def main():
    #escribe tu código abajo de esta línea
    saldoanterior = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el numero de cheques: "))
    saldoactual = saldoanterior + ingresos - egresos - (cheques * 13)
    total = saldoactual - (saldoactual * 0.075)
    print("El saldo final de la cuenta es: " + str(total))
    pass



if __name__ == '__main__':
    main()
