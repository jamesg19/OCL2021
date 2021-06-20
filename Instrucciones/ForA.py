from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class ForA(Instruccion):
    def __init__(self,asginacion, condicion,actualiza, instrucciones, fila, columna):
        self.asginacion=asginacion
        self.condicion = condicion
        self.actualiza=actualiza
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):

        #ASIGNA VALOR
        
        asginacion=self.asginacion.interpretar(tree, table)
        if isinstance(asginacion, Excepcion): return asginacion
        


        while True:

            #verifica que se cumpla la condicion
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion
            
            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsolaError(result.toString())
                        #SI HAY UN BREAK SALE DEL CICLO FOR
                        if isinstance(result, Break): return None
                else:
                    break
                
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            #ACTUALIZA LA VARIABLE
            actualiza=self.actualiza.interpretar(tree, table)
            if isinstance(actualiza, Excepcion): return actualiza