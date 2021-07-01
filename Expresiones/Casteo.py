from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorLogico

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = tipo


    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)


        #**********************************************CATEO DOUBLE**********************************************
        # (DOUBLE)  INT
        # (DOUBLE)  CHAR
        # (DOUBLE)  STRING
        #(SELF.TIPO)
        if self.tipo == TIPO.DECIMAL:
            # (DOUBLE) ENTERO
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (DOUBLE) INT.", self.fila, self.columna)
            # (DOUBLE) STRING        
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (DOUBLE) STRING.", self.fila, self.columna)
            # (DOUBLE) CHAR
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (DOUBLE) CHAR.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para (Double).", self.fila, self.columna)

        #**********************************************CATEO INT**********************************************
        # (INT)  DOUBLE
        # (INT)  CHAR
        # (INT)  STRING
        #(SELF.TIPO)
        if self.tipo == TIPO.ENTERO:
            # (INT ) DOUBLE
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (INT) DOUBLE.", self.fila, self.columna)
            # (INT ) STRING
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (INT) STRING.", self.fila, self.columna)
            # (INT ) CHAR
            elif self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (INT) CHAR.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para (INT).", self.fila, self.columna)

        #**********************************************CATEO STRING**********************************************
        # (STRING)  INT
        # (STRING)  DOUBLE

        #(SELF.TIPO)
        if self.tipo == TIPO.CADENA:
            # (STRING ) INT
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (STRING) INT.", self.fila, self.columna)
            # (STRING ) DOUBLE
            elif self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (STRING) DOUBLE.", self.fila, self.columna)
            
            return Excepcion("Semantico", "Tipo Erroneo de casteo para (STRING).", self.fila, self.columna)

        #**********************************************CATEO CHAR**********************************************
        # (CHAR)  INT
        if self.tipo == TIPO.CHARACTER:
            # (CHAR ) INT
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para (CHAR) INT.", self.fila, self.columna)
            
            return Excepcion("Semantico", "Tipo Erroneo de casteo para (CHAR).", self.fila, self.columna)
        #**********************************************CATEO BOOLEAN**********************************************
        # (BOOLEAN)  STRING
        if self.tipo == TIPO.BOOLEANO:
            # (BOOLEAN ) STRING
            if self.expresion.tipo == TIPO.CADENA:
                try:
                    if val.lower()=="false":
                        print("es falso")
                        self.expresion.tipo=TIPO.BOOLEANO
                        return False
                    elif val.lower()=="true":
                        self.expresion.tipo=TIPO.BOOLEANO
                        print("es true")
                        return True
                    else:
                        return Excepcion("Semantico", "No se puede castear para (BOOLEAN) STRING...", self.fila, self.columna)

                except:
                    return Excepcion("Semantico", "No se puede castear para (BOOLEAN) STRING.", self.fila, self.columna)
            
            return Excepcion("Semantico", "Tipo Erroneo de casteo para (BOOLEAN).", self.fila, self.columna)

        
        

    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)