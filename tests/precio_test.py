from src.app import extraer_productos
import os



def test_precio():
    assert not (os.path.exists("productos.csv"))
    datos = extraer_productos("https://diaonline.supermercadosdia.com.ar/almacen?page=2")
    assert(len(datos) > 1)
    assert("titulo" in datos[0])
    assert("precio" in datos[0])
    assert (os.path.exists("productos.csv"))



#verificar que la funcion no exista, ejecutar la funcion y verificar que exista