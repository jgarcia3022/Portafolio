def calcular_area(r):
    area = 3.1416 * r ** 2
    return area


def calcular_circunferencia(r):
    circunferencia = 2 * 3.1416 * r
    return circunferencia


def imprimir_resultado(a, c):
    print("El area es %.2f cm2" % a)
    print("La circunferencia es %.2f cm" % c)
