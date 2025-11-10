from src.app import extraer_productos, extraer_precio
import pandas as pd

def test_precio():
    datos = extraer_productos("https://diaonline.supermercadosdia.com.ar/")
    print(datos)

    productos_filtrados = []
    for p in datos:
        titulo = p['titulo']
        precio = extraer_precio(p['precio'])
        productos_filtrados.append({'titulo': titulo, 'precio': precio})
        print("-----------------------------------------------------")
        print(productos_filtrados)

    df = pd.DataFrame(productos_filtrados)
    df.to_csv("productos.csv", index=False, encoding="utf-8-sig")
    print(f"CSV generado con {len(df)} productos")


    # Convertir a DataFrame y guardar CSV
    df = pd.DataFrame(productos_filtrados)
    df.to_csv("productos_limpios.csv", index=False, encoding="utf-8-sig")
    print(f"CSV generado con {len(df)} productos")
