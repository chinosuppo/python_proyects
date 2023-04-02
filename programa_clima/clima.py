import requests
from pprint import  pprint

key_API = "05dcd8a9aea3f103ff78da30dfee6f13"

ciudad = input("Ingrese una ciudad: ")

url = "http://api.openweathermap.org/data/2.5/weather?appid=" + key_API+"&q=" + ciudad

datos_clima = requests.get(url).json()
pprint(datos_clima)