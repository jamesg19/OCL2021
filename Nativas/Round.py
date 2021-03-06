from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
import math

#DEVUELVE UN ENTERO
class Round(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value
        if self.tipo == None:
                if isinstance(value,float):#DECIMAL
                    self.tipo=TIPO.ENTERO
                elif isinstance(value,int):#ENTERO
                    self.tipo=TIPO.ENTERO
                    
                else:
                   return Excepcion("Semantico", "Tipo de parametro de Round no es numerico.", self.fila, self.columna) 
            
        
        #retorna el valor redondeado segun los decimales ingresados
        return round(value)
    #getNodo para AST
    def getNodo(self):
        nodo = NodoAST("ROUND")
        #nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo 
    