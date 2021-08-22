def main():
    #escribe tu código abajo de esta línea
    pesoinicial = float(input("Escribe el peso inicial: "))
    pesofinal = float(input("Escribe el peso final: "))
    meses = int(input("Escribe la cantidad de meses: "))
    pesopormes = (pesoinicial - pesofinal)/meses
    print("El peso que debes de bajar por mes es: " + str(pesopormes))
    pass



if __name__ == '__main__':
    main()
