import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input("Area a pintar en metros: "))
    cantidad = float(input("Rendimiento (m2/l): "))
    litrosPin = math.ceil(area/cantidad)
    print("Litros a comprar: "+str(litrosPin))
if __name__ == '__main__':
    main()
