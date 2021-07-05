
from Instrucciones.MiniConsola import MiniConsola
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table):
        
        LECTURA_VAL =MiniConsola()
        valorIngresado= LECTURA_VAL.getValor()
        return valorIngresado
        
                        

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo