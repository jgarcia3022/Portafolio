def calcular_area(r):
    area = 3.1416 * r ** 2
    return area

def calcular_circunferencia(r):
    circunferencia = 2 * 3.1416 * r
    return circunferencia

def imprimir_resultado(a,c):
    print("El area es %.2f cm2" % a)
    print("La circunferencia es %.2f cm" % c)


if __name__ == '__main__':
    print("CALCULADORA DEL CIRCULO")
    radio = float(input("Radio: "))
    area = calcular_area(radio)
 #   circunferencia = calcular_circunferencia(radio)
 #   imprimir_resultado(area, circunferencia)

    imprimir_resultado(calcular_area(radio), calcular_circunferencia(radio))
