from nodo_pieza import nodo_pieza
from pieza import pieza
import os

class lista_piezas:
    def __init__(self):
        self.primero = None
        self.columnas=0
        self.filas=0
        self.contador_de_piezas=0

    def insertar_dato(self, pieza):
        if self.primero is None:
            self.primero = nodo_pieza(pieza = pieza) # Si la lista está vacía, el primer nodo es el nuevo nodo
            self.contador_de_piezas+=1 
        else:
            actual = self.primero # Si la lista no está vacía, se crea un nodo actual que apunta al primer nodo
            while actual.siguiente: 
                actual = actual.siguiente 
            actual.siguiente = nodo_pieza(pieza = pieza) 
            self.contador_de_piezas+=1            

    def inicializar_tablero(self, filas, columnas):
        for i in range(1, filas+1):
            for j in range(1, columnas+1):
                self.insertar_dato(pieza(i,j,"White"))



    def actualizar_pieza(self, fila, columna, color):
        actual=self.primero
        while actual!= None:
            if actual.pieza.fila==fila and actual.pieza.columna==columna:
                actual.pieza.color=color
                print("Pieza actualizada")
                return
            actual=actual.siguiente
        print("Pieza no encontrada")

    def devolver_color_de_pieza(self, fila, columna):
        actual = self.primero
        while actual != None:
            if actual.pieza.fila == fila and actual.pieza.columna == columna:
                return actual.pieza.color
            actual = actual.siguiente

    def imprimir_tablero_en_consola(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                color = self.devolver_color_de_pieza(i, j)
            
                if color == "White":
                    print("| |", end="\t")
                elif color == "Blue":
                    print("|A|", end="\t")
                elif color == "Red":
                    print("|R|", end="\t")
                elif color == "Green":
                    print("|V|", end="\t")
                elif color == "Purple":
                    print("|P|", end="\t")
                elif color == "Orange":
                    print("|N|", end="\t")
                else:
                    print("| |", end="\t")                    
                #print(self.devolver_color_de_pieza(i,j),end="\t")
            print("")
        print("")     

    def graficar(self):
        f = open('aa.dot','w')
        texto="digraph G {\n node [shape=plaintext];\nlabel=\"Colorealo Guatematel\";\nsome_node [\nlabel=<\n<table border=\"0\" cellborder=\"1\" cellspacing=\"4\" width=\"100%\" height=\"100%\">\n"
    
    
        for i in range(1, self.filas + 1):
            texto+="<tr>\n"
            for j in range(1, self.columnas + 1):
                texto+="<td bgcolor=\""+self.devolver_color_de_pieza(i,j)+"\" width=\"5\" height=\"5\">"+"        "+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>\n];\n}"

        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng aa.dot -o Tablero.png')
        print("Tablero Graficado")               