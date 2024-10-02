import requests
import sys

def getUsuarios(url):
    try:
        respuesta=requests.get(url)

        if(respuesta.status_code == 200):

            usuarios=respuesta.json()
            nombres=[usuario["nombre"] for usuario in usuarios]
            return nombres
        else:
            print("Error de conexión!!")
    except Exception as error:
        print("Error!!: "+error)

def escribirArchivo(nombres,nombre_archivo):
    with(open(nombre_archivo,"w") as archivo):
        for nombre in nombres:
            archivo.write(nombre+"\n")


api=sys.argv[1]

nombres=getUsuarios(api)

for nombre in nombres:
    print(nombre)

escribirArchivo(nombres,'ejemplo')
