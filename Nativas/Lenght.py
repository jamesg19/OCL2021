from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
import math

#DEVUELVE UN ENTERO
class Lenght(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value
        if self.tipo == None:

                if isinstance(value,str):# CADENA
                    
                    self.tipo=TIPO.ENTERO

                elif isinstance(value,list):
                    self.tipo=TIPO.ENTERO
                  
                else:
                   return Excepcion("Semantico", "Tipo de parametro de LENGHT no es cadena.", self.fila, self.columna) 
        num=len(value)
        return int(num)
    #getNodo para AST
    def getNodo(self):
        nodo = NodoAST("LENGTH")
        #nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo 
    