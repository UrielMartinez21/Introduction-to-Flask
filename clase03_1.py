from flask import Flask

# --> Explicacion
# __name__ es una variable que Python crea en cada archivo
# que se ejecuta. Si el archivo se ejecuta directamente,
# Python le asigna el valor __main__. En cambio, si el
# archivo es importado, Python le asigna el nombre del
# archivo.

# app = Flask(__name__) crea una instancia de la clase
# Flask, y le pasa como parametro el valor de __name__.
app = Flask(__name__)

# --> Ruta por defecto
@app.route('/')
def hello_networkers():
    return '¡Hola Mundo con Flask!'


if __name__ == '__main__':
    # --> Ejecuta el servidor web
    app.run(host='0.0.0.0', debug=True)


