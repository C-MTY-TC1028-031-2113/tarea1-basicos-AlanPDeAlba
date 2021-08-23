def main():
    #escribe tu código abajo de esta línea
    materia1 = float(input("Escribe la calificación de la primera materia: "))
    materia2 = float(input("Escribe la calificación de la segunda materia: "))
    materia3 = float(input("Escribe la calificación de la tecera materia: "))
    materia4 = float(input("Escribe la calificación de la cuarta materia: "))
    promedio = (materia1 + materia2 + materia3 + materia4)/4
    print("El promedio es: " + str(promedio))  
    pass



if __name__ == '__main__':
    main()
