def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    primerax = float(input("Escribe x1: "))
    primeray = float(input("Escribe y1: "))
    segundax = float(input("Escribe x2: "))
    segunday = float(input("Escribe y2: "))
    pendiente = (segunday - primeray)/(segundax - primerax)
    print("La pendiente es: " + str(pendiente))
    pass



if __name__ == '__main__':
    main()
