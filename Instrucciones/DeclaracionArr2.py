from re import A
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
import copy


class DeclaracionArr2(Instruccion):
    
    def __init__(self, tipo, dimensiones, identificador, expresiones, fila, columna):
        self.identificador = identificador
        self.tipo = tipo
        self.dimensiones = dimensiones
        self.expresiones = expresiones
        self.fila = fila
        self.columna = columna
        self.arreglo = True


    def interpretar(self, tree, table):
        arreglo=[]
        print(f" TIPO1= {self.tipo} DIMENSION: {self.dimensiones} IDENTIFICADOR: {self.identificador} ")
        print(f" CANT EXPRESIONES = {len(self.expresiones)}  ")
        #print(f" EXPRESIONES_DENTRO: {(self.expresiones.value)} ")
        
        dimensiones = self.crearDimensiones2(self.expresiones,0)

        #if self.dimensiones != len(self.expresiones):   #VERIFICACION DE DIMENSIONES
            #return Excepcion("Semantico", "Dimensiones diferentes en Arreglo.", self.fila, self.columna)

        if self.dimensiones == dimensiones:

            # CREACION DEL ARREGLO
            value = self.crearDimensiones(tree, table, self.tipo, copy.copy(self.expresiones))     #RETORNA EL ARREGLO DE DIMENSIONES
            
            if isinstance(value, Excepcion): return value
            simbolo = Simbolo(str(self.identificador), self.tipo, self.arreglo, self.fila, self.columna, value)
            
            simbolo.arreglo=True
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
            return None
        

        if self.dimensiones != dimensiones:
            return Excepcion("Semantico", "Dimensiones diferentes en Arreglo.", self.fila, self.columna)


    def crearDimensiones(self, tree, table, tipo, expresiones):
        arr = []
        if len(expresiones) == 0:
            return None
        dimension = expresiones.pop(0)
        if isinstance(dimension,list):
            #Obtiene la dimension
            listaa=len(dimension)
            while listaa !=0:
                arreglo=self.crearDimensiones(tree, table, tipo, dimension)
                arr.append(arreglo)
                listaa= listaa-1
        else:
            value=dimension.interpretar(tree,table)
            if isinstance(value, Excepcion): return value

            if self.tipo == dimension.tipo:
                return value
            if self.tipo != dimension.tipo:
                return Excepcion("Semantico","Tipo de dato diferente en ARREGLO Tipo 2",self.fila,self.columna)
        return arr    
                


    def crearDimensiones2(self, expresion, contador):
    
        if isinstance(expresion, list):
            if isinstance(expresion[0], list):
                contador = contador+1
                return self.crearDimensiones2(expresion[0], contador)
            else:
                return contador
    # GET NODO EN AST
    def getNodo(self):
        nodo = NodoAST("DECLARACION ARREGLO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.dimensiones))
        nodo.agregarHijo(str(self.identificador))

        return nodo



