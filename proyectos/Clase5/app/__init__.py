from app.circulo import *

if __name__ == '__main__':
    print("CALCULADORA DEL CIRCULO")
    radio = float(input("Radio: "))
    area = calcular_area(radio)
    circunferencia = calcular_circunferencia(radio)
    imprimir_resultado(area, circunferencia)