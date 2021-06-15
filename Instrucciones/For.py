from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class For(Instruccion):
    #               for ( declaracion : condicion ; acualizacion )
    def __init__(self,declaracion, condicion,actualiza, instrucciones, fila, columna):
        self.declaracion=declaracion
        self.condicion = condicion
        self.actualiza=actualiza
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
        declaracion=self.declaracion.interpretar(tree, nuevaTabla)
        if isinstance(declaracion, Excepcion): return declaracion


        #verifica que se cumpla la condicion
        try:
            condicion = self.condicion.interpretar(tree, nuevaTabla)
            if isinstance(condicion, Excepcion): return condicion
        except:
            return condicion
            
        if self.condicion.tipo == TIPO.BOOLEANO:

            if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION

                for instruccion in self.instrucciones:
                    result = instruccion.interpretar(tree, nuevaTabla) #EJECUTA INSTRUCCION ADENTRO DEL IF
                    if isinstance(result, Excepcion) :
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    #SI HAY UN BREAK SALE DEL CICLO FOR
                    if isinstance(result, Break): return None
            else:
                break
                
        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
        #ACTUALIZA LA VARIABLE
        actualiza=self.actualiza.interpretar(tree, nuevaTabla)
        if isinstance(actualiza, Excepcion): return actualiza