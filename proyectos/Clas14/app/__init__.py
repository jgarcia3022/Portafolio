import requests

#respuesta = requests.get("http://api.open-notify.org/astros.json")
#print(respuesta.text)


parametros = {"lat": 9.0, "lon": 79.25}

respuesta = requests.get("http://api.open-notify.org/iss-pass.json", params=parametros)
print(respuesta.content)

data = respuesta.json()
print(data)