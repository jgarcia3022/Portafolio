from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Xopa Laope..!'

@app.route('/hola/<nombre>')
def hola_laope(nombre):
    return 'Xopa Laope, %s!!' % nombre

@app.route('/blog/<int:idEntrada>')
def mostrar_blog(idEntrada):
    return 'Entrada #%d' % idEntrada

@app.route('/itbms/<float:subtotal>')
def calcular_itbms(subtotal):
    return 'Impuesto de $%.2f, es $%.2f'  % (subtotal, subtotal*0.07)


if __name__ == '__main__':
    app.run()


