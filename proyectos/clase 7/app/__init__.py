from model.Participante import Participante #se importo la lista participante
import re

if __name__ == "__main__":
    listsParticipantes = []
    while(True):
        print("\n\nASISTENCIA EVENTO")
        print("1. Ingresar participante")
        print("2. Ver estadisiticas")
        print("3. Ver todos los participantes")
        print("4. Salir")
        try:
            opc = int(input("OPCION>"))
        except:
            opc = 0

        if opc == 1:
            print("\nIngresar participante")
            while (True):
                nombre = input("Nombre y Apellido:") #falta validar
                if re.search("^[A-Z][a-z]*(\s[A-Z][a-z]*)?$",nombre):
                    break
                else:
                    print("ERROR :: NOMBRE NO VALIDO")
            while (True):
                try:
                    edad = int(input("Edad: "))
                except:
                    edad = 0
                if edad > 0:
                    break
                else:
                    print("ERROR :: EDAD NO VALIDO")
            while (True):
                sexo = input("Sexo(M\F): ")
                if sexo.upper() == "M" or sexo.upper() == "F":
                    break
                else:
                    print("ERROR :: SEXO NO VALIDO")

            participante = Participante(nombre,edad,sexo)
            listsParticipantes.append(participante) #se utiliza append para ingresar los elementos a la lista

        elif opc == 2:
            masculino = 0
            femenino = 0
            mayoredad = 0
            print("\nVer estadisticas")
            print("Total de Participantes: " + str(len(listsParticipantes)))
            for p in listsParticipantes:
                if p.get_sexo() == "M":
                    masculino += 1
                else:
                    femenino += 1
                if p.get_edad() >= 18:
                    mayoredad += 1
            print("Total de Hombres: " + str(masculino))
            print("Total de Mujeres: " + str(femenino))
            print("Total de mayores de edad: " + str(mayoredad))

        elif opc == 3:
            print("Ver todos\n")
            print(len(listsParticipantes))
            for p in listsParticipantes:
                p.mostrar()
        elif opc == 4:
            break
        else:
            print("ERROR")
