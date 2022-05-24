"""Funcion para grabar datos de pedido"""
def grabar_datos(nombre, apellidos):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre+ " " + apellidos + "\n")
        file.close()
