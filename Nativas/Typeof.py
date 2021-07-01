from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO


class Typeof(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
    
    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table) 
        if isinstance(value, Excepcion) :
            return value
        if self.tipo == None:
                if isinstance(value,str):#CADENA
                    self.tipo=TIPO.CADENA
                    return "TIPO: CADENA"
                elif isinstance(value,bool):#BOOLEANO
                    self.tipo=TIPO.CADENA
                    return "TIPO: BOOLEANO"
                elif isinstance(value,int):#INTEGER
                    self.tipo=TIPO.CADENA
                    return "TIPO: ENTERO"
                elif isinstance(value,float):#DECIMAL
                    self.tipo=TIPO.CADENA
                    return "TIPO: DECIMAL"
                else :#CHAR:
                    self.tipo=TIPO.CADENA
                    return "TIPO: CHAR"

    def getNodo(self):
        nodo = NodoAST("TYPEOF")
        #nodo.agregarHijo(str(self.identificador))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo
                    
                    
            
        
        
    