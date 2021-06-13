
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import *

class Decremento(Instruccion):
    def __init__(self,  id, fila, columna):
        self.id      = id
        self.fila    = fila
        self.columna = columna
        self.tipo    = None
    #interpretar un decremento
    def interpretar(self, tree, table):

        simbolo = table.getTabla(self.id)
        if simbolo == None:
            return Excepcion("Semantico",("IDENTIFICADOR no encontrado: "+str(self.id)),self.fila,self.columna)
        
        if simbolo.tipo == TIPO.DECIMAL or simbolo.tipo == TIPO.ENTERO:
            self.tipo = simbolo.tipo
            simbolo.valor = simbolo.valor-1
            table.actualizarTabla(simbolo)
            return simbolo.valor
        else:                    
            return Excepcion("Semantico",("Ne necesita dato numerico"+str(self.id)),self.fila,self.columna)