# Introduccione de datos

# Programa para aprender sintaxis basica de Python

while True:
    nombre = input("nombre: ")
    edad = int(input("edad: "))

    print("Bienvenido, " + nombre + ". Tines " + str(edad) + " años.")

    if edad < 18:
        print("\nEstas castigado")
    elif edad == 18:
        print("\nPuedes salir\tPero ven temprano")
    else:
        print("\nLarga a trabajar")

    salida = input("Desea continuar(S/N): ")
    if salida != "S" or  salida != "S":
        break

print('Ciao')