from Instrucciones.Continue import Continue
from Instrucciones.Return import Return
from Abstract.NodoAST import NodoAST
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
        self.hayContinue=False
        self.columna = columna

    def interpretar(self, tree, table):
        
        nuevaTabla = TablaSimbolos(table)       #NUEVO ENTORNO
        #nuevaTabla2 = TablaSimbolos(table)       #NUEVO ENTORNO2
        declaracion=self.declaracion.interpretar(tree, nuevaTabla)
        if isinstance(declaracion, Excepcion): 
            return declaracion

        while True:
            nuevaTabla2 = TablaSimbolos(nuevaTabla)       #NUEVO ENTORNO2
            #verifica que se cumpla la condicion
            try:
                condicion = self.condicion.interpretar(tree, nuevaTabla2)
                if isinstance(condicion, Excepcion): return condicion
            except:
                
                return condicion
            
            if self.condicion.tipo == TIPO.BOOLEANO:
                
                if bool(condicion) == True:   # VERIFICA SI ES VERDADERA LA CONDICION
                    
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla2) #EJECUTA INSTRUCCION ADENTRO DEL IF
                        if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsolaError(result.toString())
                    
                        #SI HAY UN CONTINUE
                        if isinstance(result, Continue): 
                            self.hayContinue=True
                            actualiza=self.actualiza.interpretar(tree, nuevaTabla2)
                            if isinstance(actualiza, Excepcion): return actualiza
                            break
                            
                        #SI HAY UN BREAK SALE DEL CICLO FOR
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                        
                        
                else:
                    break
                
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            if self.hayContinue==True: 
                self.hayContinue=False
                print(" CONTINUEEEEE............")
                #ACTUALIZA LA VARIABLE
                #actualiza=self.actualiza.interpretar(tree, nuevaTabla2)
                #if isinstance(actualiza, Excepcion): return actualiza
                continue

            print("ANALIZA  ")
            #ACTUALIZA LA VARIABLE
            actualiza=self.actualiza.interpretar(tree, nuevaTabla2)
            if isinstance(actualiza, Excepcion): return actualiza


    def getNodo(self):
        nodo = NodoAST("FOR")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo
        