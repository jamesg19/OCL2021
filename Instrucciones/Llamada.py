from TS.Tipo import TIPO
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from TS.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion


class Llamada(Instruccion):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        # VERIFICA SI LA FUNCION EXISTE Y LA OBTIENE
        result = tree.getFuncion(self.nombre.lower()) ## OBTENER LA FUNCION
        if result == None: # NO SE ENCONTRO LA FUNCION
            return Excepcion("Semantico", "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)
        # CREAR UN NUEVO AMBITO O ENTORNO PARA LA FUNCION
        nuevaTabla = TablaSimbolos(table)
        # OBTENER PARAMETROS
        if len(result.parametros) == len(self.parametros): #LA CANTIDAD DE PARAMETROS ES LA ADECUADA
            contador=0
            #
            for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
                
                resultExpresion = expresion.interpretar(tree, nuevaTabla)
                if isinstance(resultExpresion, Excepcion): return resultExpresion
                
                print("********1*******")
                print(expresion.tipo)
                print(result.parametros[contador]["tipo"])
                    
                # COMPARA EL TIPO DE VARIABLE DEL PARAMETRO DE LA FUNCION CON EL TIPO DE PARAMETRO QUE SE ENVIA EN LA LLAMADA
                if result.parametros[contador]["tipo"] == expresion.tipo:  # VERIFICACION DE TIPO
                    
                    # CREACION DE SIMBOLO E INGRESARLO A LA TABLA DE SIMBOLOS
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipo'], self.fila, self.columna, resultExpresion)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion): return resultTabla

                else:
                    return Excepcion("Semantico", "Tipo de dato diferente en Parametros de la llamada.", self.fila, self.columna)
                contador += 1

        else: 
            return Excepcion("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)

        value = result.interpretar(tree, nuevaTabla)         # INTERPRETAR EL NODO FUNCION
        
        
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo

        return value