from menu import*
from informacion_de_los_artistas import datos_artistas
from informacion_del_genero import añadir_genero
from informacion_del_pais import añadir_pais

def main():
    while True: 
        print(menu_principal)  
        opcion = input("Seleccione una opción: ").strip()  
        if   opcion == "1": 
                    datos_artistas()
        elif opcion == "2":
                    añadir_genero()
        elif opcion == "3": 
                    añadir_pais()
        elif opcion == "4": 
                    print("Informes relevantes")
        elif opcion == "5": 
                    print("Saliendo del programa.....")
                    break
        else:  
            print("Opción inválida. Intente de nuevo.")

        
if __name__ == "__main__":
    main()  

