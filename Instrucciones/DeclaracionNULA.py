from TS.Excepcion import Excepcion
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional


class DeclaracionNULA(Instruccion):
    def __init__(self, tipo, identificador, fila, columna):
        self.identificador = identificador
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        self.tipo=TIPO.NULO
       
        value="None"

        simbolo = Simbolo(str(self.identificador), TIPO.NULO, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result
        return None

    def getNodo(self):
        nodo = NodoAST("DECLARACION NULA")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        #nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

