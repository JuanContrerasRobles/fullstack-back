"""Funcion para grabar datos de pedido"""
def grabar_datos(nombre, apellidos):
    "Recoge los datos y crea un archivo .txt con esos datos"
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre+ " " + apellidos + "\n")
        file.close()
