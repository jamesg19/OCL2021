from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO


class ToLower(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion): return value

        if self.tipo == None:
                if isinstance(value,str):#CADENA
                    self.tipo=TIPO.CADENA
                    
                else:
                   return Excepcion("Semantico", "Tipo de parametro de ToLower no es cadena.", self.fila, self.columna) 
            
        if isinstance(value, Excepcion): return value
        return value.lower()