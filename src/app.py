from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import pandas as pd



def limpiar_texto(texto):
   if texto:
       return texto.replace("\xa0", " ").replace("\n", " ").strip()
   return ""


def extraer_productos(url: str):
   productos = []

   chrome_options = Options()
   chrome_options.add_argument("--headless")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-gpu")


   service = Service("/usr/bin/chromedriver")
   driver = webdriver.Chrome(service=service, options=chrome_options)


   print(f"Intentando extraer datos de: {url}\n")
   driver.get(url)
   time.sleep(10)  # esperar que cargue JS


   # Scroll para cargar más productos
   SCROLL_PAUSA = 2
   last_height = driver.execute_script("return document.body.scrollHeight")
   while True:
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(SCROLL_PAUSA)
       new_height = driver.execute_script("return document.body.scrollHeight")
       if new_height == last_height:
           break
       last_height = new_height


   time.sleep(5)
   html = driver.page_source
   driver.quit()
   soup = BeautifulSoup(html, "html.parser")


   for producto in soup.find_all("article"):
       titulo_span = producto.select_one("h3")
       precio_span = producto.select_one("div")


       if titulo_span and precio_span:
           titulo = limpiar_texto(titulo_span.get_text())
           precio = limpiar_texto(precio_span.get_text())
           productos.append({"titulo": titulo, "precio": precio})
       else:
           print("No se pudieron extraer datos de un producto")
           
   df = pd.DataFrame(productos)
   df.to_csv("productos.csv", index=False, encoding="utf-8-sig")
   print(f"CSV generado con {len(df)} productos")

   # Convertir a DataFrame y guardar CSV
   df = pd.DataFrame(productos)
   df.to_csv("productos_limpios.csv", index=False, encoding="utf-8-sig")
   print(f"CSV generado con {len(df)} productos")

   print(f"Se extrajeron {len(productos)} productos")
   return productos


def precio_limpio(precio_texto):
   match = re.search(r'(\d{1,3}(?:\.\d{3})*,\d{2})', precio_texto)
   if match:
       return match.group(1)
   return None