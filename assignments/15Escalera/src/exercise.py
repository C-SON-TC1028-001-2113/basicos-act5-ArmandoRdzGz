import math
def main():
    #escribe tu código abajo de esta línea

    alturaCasa = float(input("Altura de la casa: "))
    angulo = int(input("Angulo en grados: "))
    seno = math.sin(math.radians(angulo))
    largo = round(alturaCasa/seno)
    print("Largo de la escalera: "+str(largo))
if __name__ == '__main__':
    main()
