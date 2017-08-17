if __name__ == '__main__':
    import re

    texto1 = 'casa'
    texto2 = 'casas'
    texto3 = 'pasa'

    if re.match(texto1, texto2):
        print("t1 y t2 coinciden")
    else:
        print("t1 y t2 no coinciden")

    if re.match(".asa", texto1):
        print("t1 termina en asa")

    if re.match("\.mp4", input("Archivo: ")):
        print("Perfecto")
    else:
        print("No me funciona")

arhivos = ['jpg','mp3','png']
for archivo in arhivos:

    if re.match('jpg|png|gif|bmp', archivo):
        print("Es una imagen")
    else:
        print("Formato invalido")