from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import *


class Incremento(Instruccion):
    def __init__(self,  id, fila, columna):
        self.id      = id
        self.fila    = fila
        self.columna = columna
        self.tipo    = None

    def interpretar(self, tree, table):
        #identificador, tipo, fila, columna, valor
        simbolo = table.getTabla(self.id)
        if simbolo == None:
            return Excepcion("Semantico",("IDENTIFICADOR no encontrado: "+str(self.id)),self.fila,self.columna)
        
        if simbolo.tipo == TIPO.DECIMAL or simbolo.tipo == TIPO.ENTERO:
            self.tipo = simbolo.tipo
            simbolo.valor = simbolo.valor+1
            table.actualizarTabla(simbolo)
            return simbolo.valor
        else:                    
            return Excepcion("Semantico",(" EL INCREMENTO DEBE SER VAR ENTERO O DECIMAL "+str(self.id)),self.fila,self.columna)