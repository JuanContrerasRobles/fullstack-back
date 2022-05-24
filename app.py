""" Se importan funciones y datos desde la libreria"""
from flask import Flask, request, redirect
from grabar_datos import grabar_datos

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])

def datos():
    """Funcion que recoge los datos a traves del metodo POST"""
    if request.method == "POST":
        nombre = request.form.get("Nombre")
        apellidos = request.form.get("Apellidos")
        usuario = nombre + " " + apellidos
        grabar_datos(nombre, apellidos)
        print(usuario)
    return redirect ("http://localhost/solicita_pedido.html", code=302)