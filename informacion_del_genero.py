import json
import os

def cargar_datos():
    global genero
    try:
        with open('generos.json', 'r') as archivo:
            genero =json.load(archivo)
    except FileNotFoundError:
        genero = []
    except json.JSONEncoder:
        genero = []
        if os.path.exists(archivo):  
            with open(archivo, 'r') as f:  
                return json.load(f)  
    return {}  

def guardar_datos():
    with open('generos.json', 'w') as archivo: 
        json.dump(genero, archivo, indent=4) 

def añadir_genero():
    cargar_datos()
    ID_del_género = input("Ingrese el ID del genero que desea añadir: ")
    Descripción_del_género = input("Ingrese la descripcion del genero: ")
    genero2={
    'El ID Del Genero es': ID_del_género,
    'La Descripcion Del Genero es': Descripción_del_género,
    }
    genero.append(genero2)
    guardar_datos()

  
