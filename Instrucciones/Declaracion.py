from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional


class Declaracion(Instruccion):
    def __init__(self, tipo, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        try:
            #LE ASIGNO EL TIPO DE VARIABLE SEGUN LOS VALORES DE LA EXPRESION IGUALADA
            self.tipo=self.expresion.tipo

            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable

            #SI LA EXPRESION CONTIENE UNA OPERACION var variableP = 10+20+var1
            #determina el valor de variableP y determina el tipo de dato(integer, string, boolean, char o decimal)
            if self.tipo == None:
                if isinstance(value,chr):#CHAR
                    self.tipo=TIPO.CHARACTER
                elif isinstance(value,chr):#CADENA:
                    self.tipo=TIPO.CADENA
                elif isinstance(value,int):#INTEGER
                    self.tipo=TIPO.ENTERO
                elif isinstance(value,float):#DECIMAL
                    self.tipo=TIPO.DECIMAL
                elif isinstance(value,bool):#BOOLEANO
                    self.tipo=TIPO.BOOLEANO
                

            
            if isinstance(value, Excepcion): return value

            #if self.tipo != self.expresion.tipo:
                #return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

            simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)

            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): return result
            return None
        except:
            print("ENTRA EN EXCEPT!!")
            self.tipo=None
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            #SI LA EXPRESION CONTIENE UNA OPERACION var variableP = 10+20+var1
            #determina el valor de variableP y determina el tipo de dato(integer, string, boolean, char o decimal)
            if self.tipo == None:

                if isinstance(value,str):#CADENA
                    self.tipo=TIPO.CADENA
                elif isinstance(value,int):#INTEGER
                    self.tipo=TIPO.ENTERO
                elif isinstance(value,float):#DECIMAL
                    self.tipo=TIPO.DECIMAL
                elif isinstance(value,bool):#BOOLEANO
                    self.tipo=TIPO.BOOLEANO
                else:
                    self.tipo=TIPO.CHARACTER

            if isinstance(value, Excepcion): return value

            #if self.tipo != self.expresion.tipo:
                #return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

            simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)

            result = table.setTabla(simbolo)

            if isinstance(result, Excepcion): return result
            return None
            
