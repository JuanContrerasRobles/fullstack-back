""" Pruebas Grabar Datos"""
import grabar_datos

def test_grabar_datos():
    """ Prueba general"""
    with open("pedidos.txt","w",encoding="utf-8")as file:
        grabar_datos.grabar_datos("Pedro","Gil de Diego")
        grabar_datos.grabar_datos("Michael","Jordan")
        firstline = file.readline()
        secondline = file.readline()
        file.close()
    assert firstline == "-Pedro Gil de Diego\n"
    assert secondline == "-Michael Jordan\n"
