from Abstract.Instruccion import Instruccion
from TS.Excepcion         import Excepcion
from TS.Tipo              import TIPO
from TS.Tipo              import OperadorRelacional
from TS.TablaSimbolos     import TablaSimbolos
from Expresiones.Relacional     import Relacional
from Abstract.NodoAST import NodoAST

class Switch(Instruccion):
    def __init__(self, expresion, lst_case,default, fila, columna):
        self.expresion= expresion
        self.lst_case= lst_case
        self.default= default
        self.fila= fila
        self.columna= columna

    def interpretar(self, tree, table):
        print("INTERPRETA")
        #si la lista de casos en nula
        if self.lst_case == None:
            #si default no es nulo lo ejecuta
            if self.default != None:
                self.default.interpretar(tree,table)
        else:
            
            #si la lista de casos contiene alguno
            result = False
            
            #lee todos los casos con el for
            for case in self.lst_case:
                #obtiene el valor del case
                value_case = case.expresion.interpretar(tree,table)
                if isinstance(value_case, Excepcion): return value_case
                #obtiene el valor del switch
                value_expresion = self.expresion.interpretar(tree,table)
                if isinstance(value_expresion,Excepcion): return value_expresion
                
                if str(value_expresion) == str(value_case):
                    #si el valor de la expresion es igual al valor de la expresion switch
                    #interpreta el case 
                    result = case.interpretar(tree, table)
                    if isinstance(result, Excepcion) :
                            tree.getExcepciones().append(result)
                            tree.updateConsolaError(result.toString())
                    
                    #break
                    if result:
                        break
                
            if not(result): # si result  == true --> el caso evaluado trae break
                if self.default != None:
                    self.default.interpretar(tree,table)


    def getNodo(self):
        nodo = NodoAST("SWITCH")

        lst_cases = NodoAST("LISTA_CASE")
        for instr in self.lst_case:
            lst_cases.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(lst_cases)
        
        if self.default != None:
            default = NodoAST("INSTRUCCIONES DEFAULT")
            default.agregarHijoNodo(instr.getNodo())
            nodo.agregarHijoNodo(default) 
        return nodo





    