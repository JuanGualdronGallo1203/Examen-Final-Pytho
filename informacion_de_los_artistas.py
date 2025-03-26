import json
import os

def cargar_datos():
    global artistas
    try:
        with open('artistas.json', 'r') as archivo:
            artistas=json.load(archivo)
    except FileNotFoundError:
        artistas = []
    except json.JSONEncoder:
        artistas = []
        if os.path.exists(archivo):  
            with open(archivo, 'r') as f:  
                return json.load(f)  
    return {}  

def guardar_datos():
    with open('artistas.json', 'w') as archivo: 
        json.dump( artistas, archivo, indent=4) 


def datos_artistas():
    nombre = input("Ingrese el nombre del artista: ")
    pais =  input("Ingrese el nombre del pais de origen y su ISO3: ")
    años = input("Ingrese los años de actividad del artista: ")
    año_de_lanzamiento = input("Ingrese el años de lanzamiento del artista: ")
    género_musical = input("Ingrese el genero musical del artista: ")
    
    while True:
        try:
            unidades_certificadas_totales = input("Ingrese las unidades totales certificadas del artista: ")
            break
        except ValueError:
            print("OPCION NO VALIDA, POR FAVOR INTENTE DE NUEVO!!!!")
            continue

    while True:
        try:
            ventas_reclamadas = input("Ingrese las ventas del artista: ")
            break
        except ValueError:
            print("OPCION NO VALIDA, POR FAVOR INTENTE DE NUEVO!!!!")
            continue
        
    estado_del_artista = input("Ingrese el estado del artista (Si=Esta activo o No=Esta retirado)")

    artista={
        'Nombre del artista': nombre,
        'Pais De Origen Del Artista': pais,
        'Anios de actividad Del Artista son': años,
        'Anio De Lanzamiento Del Artista': año_de_lanzamiento,
        'El Genero Musical Del artista es': género_musical,
        'Las unidades certificadas son': unidades_certificadas_totales,
        'Las Ventas Reclamadas Del Artista Son': ventas_reclamadas,
        'El estado De Actividad Del artista es': estado_del_artista
           }
    cargar_datos()
    artistas.append(artista)
    guardar_datos()
