import json
import os

def cargar_datos():
    global paises
    try:
        with open('paises.json', 'r') as archivo:
            paises =json.load(archivo)
    except FileNotFoundError:
        paises = []
    except json.JSONEncoder:
        paises = []
        if os.path.exists(archivo):  
            with open(archivo, 'r') as f:  
                return json.load(f)  
    return {}  

def guardar_datos():
    with open('paises.json', 'w') as archivo: 
        json.dump(paises, archivo, indent=4) 

def añadir_pais():
    cargar_datos()
    paiz = input("Ingrese el nombre del pais: ")
    codigo_iso=input("Ingrese el codigo ISO del pais: ")
    codigo_iso3=input("Ingrese el codigo ISO3 del pais: ")
    pais={
    'Nombre Del Pais': paiz,
    'El Codigo ISO es': codigo_iso,
    'El Codigo ISO3 es': codigo_iso3
    }
    paises.append(pais)
    guardar_datos()

    
