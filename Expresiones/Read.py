from Instrucciones.MiniConsola import MiniConsola
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO


class Read(Instruccion):
    def __init__(self, fila, columna, root):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA
        self.root=root

    def interpretar(self, tree, table):
        lectura_val = MiniConsola("Consola JPR JAMES",self.root)
        valor_ingresado = lectura_val.getValor()
        return valor_ingresado

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo
