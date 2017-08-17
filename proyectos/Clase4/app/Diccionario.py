# Funciones

def imprimir_lista(x):
    print("\nMi lista de Supermercado...")
    artIndice = 0
    for a in x:
        print(str((int(x.index(a)+1))) + ".  " + a)

def imprimir_diccionario(w):
    print("\nMi lista de supermercado..")
    for art, cant in w.items():
        print ("Articulo: " + str(art) + " (cantidad: " + str(cant) + ")")


if __name__ == '__main__':
# Adicion de lista -- coleccion -- arreglos
#    lista = [ ]

     diccionario {}
    while True:
        print('Lista de Supermercado')
        print('1. Agregar Elemento')
        print('2. Quitar Elemento')
        print('3. Ver lista')
        print('4. Salir')
# Manejo de Excepciones
        try:
            opc = int(input("Opcion: "))
        except ValueError:
            opc = 0
# Fin de la Excepcion

# Condicion del Ciclo

        if opc == 1:
#           print("Opcion 1")
            print("\nVamos a ingresar un articulo a la lista...")
            artInsertar = input("Articulo: ")
            if artInsertar not in diccionario:
                #lista.append(artInsertar)
            diccionario[artInsertar] = 1

            else:
#                print("Articulo ya en la lista")
            diccionario[artInsertar] +=1#            lista.append(input("Articulo: "))
        elif opc == 2:
#           print("Opcion 2")
            print("\nVamos a quitar un articulo de la lista...")
            artBorrar = input("Articulo: ")
            if artBorrar in lista:
                lista.remove(artBorrar)
            else:
                print("\nLo siento. Articulo no encontrado...")
        elif opc == 3:
#           print("Opcion 3")
            imprimir_lista(lista)
# for ciclo
      #      for articulo in lista:
      #          print(articulo)
        elif opc == 4:
            break
        else:
            print("ERROR:: Opcion no valida")
print("Hasta Luego !")
