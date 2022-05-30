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

def checksize():
    """Comprueba disponibilidad de un tamaño de pizza"""
    if request.method == "POST":
        mensaje1 = "Disponible"
        mensaje2 = "No Disponible"
        mensajes = mensaje1, mensaje2
        if request.form.get("S") == False:
            print(mensaje1)
        else:
            print(mensaje2)
    return Response(mensajes, 200,{'Access-Control-Allow-Origin': '*'})

#Este es otro tipo de codigo pero siempre me retorna disponible ⇩

"""     
def checksize():
    #Comprueba disponibilidad de un tamaño de pizza
    if request.method == "POST": 
    mensajes = {"Estado1":"Disponible","Estado2":"No disponible"}
    for valor in mensajes.values():
        if request.form.get != "S":
            print(valor)
            return valor
    return Response(valor, 200,{'Access-Control-Allow-Origin': '*'})
"""
