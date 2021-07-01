from re import A
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
import copy


class ModificarArreglo(Instruccion):
    def __init__(self, identificador, expresiones, valor, fila, columna):
        self.identificador = identificador
        self.expresiones = expresiones
        self.valor = valor
        self.fila = fila
        self.columna = columna

    #-***************************************** INTERPRETAR LA DOFICICACION DEL ARREGLO *******************************************
    def interpretar(self, tree, table):
        value = self.valor.interpretar(tree, table) # Valor a asignar a la variable
        if isinstance(value, Excepcion): return value

        simbolo = table.getTabla(self.identificador.lower())

        if simbolo == None:
            return Excepcion("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        if not simbolo.getArreglo(): 
            return Excepcion("Semantico", "Variable " + self.identificador + " no es un arreglo.", self.fila, self.columna)

        if simbolo.getTipo() != self.valor.tipo:
            tip1=self.getTIPOEXPR(str(simbolo.getTipo()))
            tip2=self.getTIPOEXPR(str(self.valor.tipo))
            return Excepcion("Semantico", f"Tipos de dato diferente en Modificacion arreglo {tip1} expresion {tip2}", self.fila, self.columna)

        # BUSQUEDA DEL ARREGLO
        value = self.modificarDimensiones(tree, table, copy.copy(self.expresiones), simbolo.getValor(), value)     #RETORNA EL VALOR SOLICITADO
        if isinstance(value, Excepcion): return value

        return value

    def getTIPOEXPR(self,cadena):
        if cadena=="TIPO.CADENA":
            cadena="STRING" 
        elif cadena=="TIPO.ENTERO":
            cadena="INT"
        elif cadena=="TIPO.DECIMAL":
            cadena="DOUBLE"
        elif cadena=="TIPO.BOOLEANO":
            cadena="BOOLEAN"
        elif cadena=="TIPO.CHARACTER":
            cadena="CHAR"
        return cadena
    #********************************Modificar las dimensiones del arreglo***************************************************
    def modificarDimensiones(self, tree, table, expresiones, arreglo, valor):
        if len(expresiones) == 0:
            if isinstance(arreglo, list):
                return Excepcion("Semantico", "Modificacion a Arreglo incompleto.", self.fila, self.columna)
            return valor
        if not isinstance(arreglo, list):
            return Excepcion("Semantico", "Accesos de más en un Arreglo.", self.fila, self.columna)
        dimension = expresiones.pop(0)
        num = dimension.interpretar(tree, table)

        if isinstance(num, Excepcion): return num
        #Verifica el tipo de arreglo

        #dimension tipo: Es el tipo de la expresion a asignar
        if dimension.tipo != TIPO.ENTERO:
            return Excepcion("Semantico", "Expresion diferente a ENTERO en Arreglo ModificarArreglo.", self.fila, self.columna)

        try:
            value = self.modificarDimensiones(tree, table, copy.copy(expresiones), arreglo[num], valor)
            print("*****//******")
            print(valor)
            print("*****//******")
            if isinstance(value, Excepcion): return value
            if value != None:
                arreglo[num] = value
        except:
            return Excepcion("Semantico", f"Índice {num}  fuera de límites para longitud del arreglo ", self.fila, self.columna)
        return None

    def getNodo(self):
        nodo = NodoAST("MODIFICACION ARREGLO")
        nodo.agregarHijo(str(self.identificador))
        exp = NodoAST("EXPRESIONES DE LAS DIMENSIONES")
        for expresion in self.expresiones:
            exp.agregarHijoNodo(expresion.getNodo())
        nodo.agregarHijoNodo(exp)
        nodo.agregarHijoNodo(self.valor.getNodo())
        return nodo
