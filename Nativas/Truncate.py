from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
import math


class Truncate(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 

        if self.tipo == None:
                if isinstance(value,float):#DECIMAL
                    self.tipo=TIPO.DECIMAL
                elif isinstance(value,int):#ENTERO
                    self.tipo=TIPO.ENTERO
                    
                else:
                   return Excepcion("Semantico", "Tipo de parametro de Truncate no es numerico.", self.fila, self.columna) 
            
        if isinstance(value, Excepcion): return value
        return math.trunc(value)
    