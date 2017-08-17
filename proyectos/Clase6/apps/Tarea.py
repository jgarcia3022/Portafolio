if __name__ == '__main__':

    import pickle

    print("\t", "Bienvenido")
    arch = open('datos.txt', 'a+')
    while True:
        apellido = input('Ingrese apellido del vendedor: ')
        nombre = input('Ingrese el Nombre del vendedor: ')
        ventas = input('Ingrese su ventas realizada: ')

        if dni < 39000000:
            print("\t", "D.N.I. MENOR A 39 MILLONES")
        lista = [nombre, apellido, ventas]
        pickle.dump(lista, arch)
        op = input("Desea continuar agregando vendedores? S/N: ")
        if op.upper() == "N":
            break
    arch.close()
    arch=open('datos.txt','r')
    print("apellido",'\t',"Nombre",'\t','\t',"ventas realizadas")

    while True:
    a=pickle.load(arch)
    except:
    break

    print "fallo"
    print(a[0],"\t\t",a[1],"\t\t",a[2],"\t\t",a[3])
    arch.close()pwd




