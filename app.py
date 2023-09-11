from lista_piezas import lista_piezas
mi_tablero = lista_piezas()

def mostrar_menu():
    print("")
    print("Bienvenido al juego Colorealo by Guatematel ")
    print("")
    print("------------- Colorealo -------------")
    print("1. Crear tablero")
    print("2. Mostrar datos del estudiante")
    print("3. Salir")
    print("------------- Guatematel -------------")
    opcion = input("Ingrese una opcion: ")
    while True:
        if opcion == "1":
            crear_tablero()
            break
        elif opcion == "2":
            mostrar_datos_del_estudiante()
            mostrar_menu()
        elif opcion == "3":
            print("Gracias por jugar")
            exit()
        else:
            print("Opcion no valida")
            opcion = input("Ingrese una opcion: ")

def mostrar_datos_del_estudiante():
    print("")
    print("------------- Colorealo -------------")
    print("Nombre: Josué Nabí Hurtarte Pinto")
    print("Carnet: 202202481")
    print("Curso: Introduccion a la programacion y computacion 2")
    print("Sección: D")
    print("------------- Guatematel -------------")
    print("")

def crear_tablero():
    print("")
    print("Creando tablero...")
    print("")
    print("------------- Colorealo -------------")   
    filas = input("ingrese el numero de filas: ")
    columnas = input("ingrese el numero de columnas: ")
    print("------------- Guatematel -------------")
    print("")
    # crear piezas del tablero
    mi_tablero.inicializar_tablero(int(filas), int(columnas))
    mi_tablero.filas = int(filas)
    mi_tablero.columnas = int(columnas)

    print("------------- Colorealo -------------")
    nueva_pieza=True
    while nueva_pieza:
        fila=input("Ingrese la fila de la pieza: ")
        columna=input("Ingrese la columna de la pieza: ")
        print("")
        print("Ingrese el color de la pieza: ")
        print("A - Azul")
        print("R - Rojo")
        print("V - Verde")
        print("P - Purpura")
        print("N - Naranja")
        color=input("Elige el color para la pieza: ")
        if color=="A":
            color="Blue"
        elif color=="R":
            color="Red"
        elif color=="V":
            color="Green"
        elif color=="P":
            color="Purple"
        elif color=="N":
            color="Orange"
        else:
            color="White"        
        mi_tablero.actualizar_pieza(int(fila),int(columna),color)
        print("")
        print("")
        mi_tablero.imprimir_tablero_en_consola()
        respuesta=input("Desea agregar otra pieza S/N: ")
        print("")
        print("")
        if respuesta=="N" or respuesta=="n":
            nueva_pieza=False
    print("------------- Guatematel -------------")
    print("")
    mi_tablero.imprimir_tablero_en_consola()
    print("------------- Colorealo -------------")
    print("")
    print("")
    # Se procede a graficar el tablero
    mi_tablero.graficar()
    print("Se ha graficado el tablero")
    print("------------- Guatematel -------------")

mostrar_menu()    