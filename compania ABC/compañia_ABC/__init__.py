def imprimir_lista(x):

    print("\n\nEl total de las ventas es: " + str(total))
    if total < millon:
        print("\n Necesitamos mejorar las ventas!!\n")
        print("El mejor de este periodo fue: " + str(nombre_alto) + "  con: " + str(alto) + "$")
        print("El mas bajo de este periodo fue: " + str(nombre_bajo) + "  con: " + str(bajo) + "$")

    else:
        print("\n Excelente trabajo sigan asi!!")
        print("\nEl mejor de este periodo fue: " + str(nombre_alto) + "  con: " + str(alto) + "$")
        print("El mas bajo de este periodo fue: " + str(nombre_bajo) + "  con: " + str(bajo) + "$")


def imprimir_diccionario(w):
    print("Vendedores")

    for art, cant in w.items():
        print("Vendedor: " + str(art) + "  Venta: " + str(cant) )


if __name__== "__main__":
    diccionario = {}
    total = 0
    millon = 1000000
    alto = 0
    bajo =0
    nombre_alto = ""
    nombre_bajo = ""

    while True:
        print("\n\nCompañia ABC ")
        print("1. Agregar vendedor")
        print("2. Ver ventas")
        print("3. Agregar venta")
        print("4. Salir")
        try:
            opc = int(input("Opcion: "))
        except ValueError:
            opc = 0

        if opc == 1:
            print("\nNuevo vendedor: ")
            nombre = input("Ingrese nombre: ")
            if nombre not in diccionario:
                diccionario[nombre] = 0
        elif opc  == 2:
            print ("\nVentas globales: ")
            imprimir_lista (nombre)
            imprimir_diccionario(diccionario)
        elif opc == 3:
            print("\n")
            while True:
                imprimir_diccionario(diccionario)
                vendAgregar = input("\nNombre del Vendedor: ")
                if vendAgregar in diccionario:
                    try:
                        op = int(input("1. Agregar venta \n2. Borrar venta anterior"))
                    except:
                        op = 0

                    if op == 1:
                        diccionario[vendAgregar] = int(input("\nMonto: "))
                        total = total + diccionario[vendAgregar]

                        if diccionario[vendAgregar] != 0 and bajo < diccionario[vendAgregar]:
                            bajo = diccionario[vendAgregar]
                            nombre_bajo = str(nombre)
                        if diccionario[vendAgregar] > alto:
                            alto = diccionario[vendAgregar]
                            nombre_alto = str(nombre)

                        break
                    elif op == 2:
                        while True:
                            try:
                                c = int(input("Cantidad: "))
                            except ValueError:
                                print("Cantidad invalida")
                            if c > 0 and c < int(diccionario[vendAgregar]):
                                diccionario[vendAgregar] -= c
                                break
                            elif c == int(diccionario[vendAgregar]):
                                del diccionario[vendAgregar]
                                break
                            else:
                                print("Cantidad invalida")
                    else:
                        print("Opcion invalida. Intente nuevamente.")
        elif opc == 4:
            break
        else:
            print("ERROR: :opcion no valida")
    print("Hasta luego")