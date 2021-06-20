from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import OperadorLogico, TIPO, OperadorAritmetico


class AsignacionNULA(Instruccion):
    def __init__(self, identificador, expresion, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = "None"
        if isinstance(value, Excepcion): 
            return value
        
        simbolo = Simbolo(self.identificador, TIPO.NULO, self.fila, self.columna, value)

        result = table.actualizarTabla(simbolo)

        if isinstance(result, Excepcion): 
            tree.getExcepciones().append(result)
            tree.updateConsolaError(result.toString())
            return result
        return None

