from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorLogico, TIPO, OperadorAritmetico

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None:
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Excepcion): return der

        #-----------------------SUMA---------------------------
        if self.operador == OperadorAritmetico.MAS: #SUMA
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                valorBoolean=self.obtenerVal(self.OperacionDer.tipo, der)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + valorBoolean
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #DECIMAL
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                valorBoolean=self.obtenerVal(self.OperacionDer.tipo, der)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + valorBoolean
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            # BOOLEANO
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                valorBoolean=self.obtenerVal(self.OperacionIzq.tipo, izq) 
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return valorBoolean + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                valorBoolean=self.obtenerVal(self.OperacionIzq.tipo, izq)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return valorBoolean + self.obtenerVal(self.OperacionDer.tipo, der) 
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                valorBoolean=self.obtenerVal(self.OperacionIzq.tipo, izq)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                valorBooleanD=self.obtenerVal(self.OperacionDer.tipo, der)
                if valorBooleanD==False:
                    valorBooleanD=0
                elif valorBooleanD==True:
                    valorBooleanD=1
                return valorBoolean + valorBooleanD
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + self.obtenerVal(self.OperacionDer.tipo, der)
            #CHAR
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CHARACTER:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CHARACTER and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            #STRING
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            elif self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CHARACTER:
                self.tipo = TIPO.CADENA
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            return Excepcion("Semantico", "Tipo Erroneo de operacion para + SUMA.", self.fila, self.columna)
        #-----------------------RESTA---------------------------
        elif self.operador == OperadorAritmetico.MENOS: #RESTA
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.ENTERO
                valorBoolean=self.obtenerVal(self.OperacionDer.tipo, der)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - valorBoolean
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.DECIMAL
                valorBoolean=self.obtenerVal(self.OperacionDer.tipo, der)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - valorBoolean
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                valorBoolean=self.obtenerVal(self.OperacionIzq.tipo, izq)
                if valorBoolean==False:
                    valorBoolean=0
                elif valorBoolean==True:
                    valorBoolean=1
                return valorBoolean - self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - RESTA.", self.fila, self.columna)
        
        #MULTIPLICACION   
        elif self.operador == OperadorAritmetico.POR: #MULTIPLICACION
            #print("ES MULTIPLIACION")
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)                
            #print("RETORNA UN ERROR")
            return Excepcion("Semantico", "Tipo Erroneo de operacion para * MULTPILICACION.", self.fila, self.columna)

        #DIVISON   
        elif self.operador == OperadorAritmetico.DIV: #DIVISON
            try:
                if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)                
                else:
                    return Excepcion("Semantico", "Tipo Erroneo de operacion para / DIVISON.", self.fila, self.columna)
            except ZeroDivisionError:
                return Excepcion("Semantico", "Tipo Erroneo de operacion para DIVISION EN 0.", self.fila, self.columna)

        #POTENCIA  
        elif self.operador == OperadorAritmetico.POT: #POTENCIA
            if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)    
            elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)                
            
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ** POTENCIA.", self.fila, self.columna)
        

        #MODULO   
        elif self.operador == OperadorAritmetico.MOD: #MODULO
            try:
                if self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)    
                elif self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL:
                    self.tipo = TIPO.DECIMAL
                    return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)                
                
                return Excepcion("Semantico", "Tipo Erroneo de operacion para % MODULO.", self.fila, self.columna)
            except:
                return Excepcion("Semantico", "error de operacion para % MODULO con 0.", self.fila, self.columna)
                
        #-----------------------NEGACION NUMERO ----------------------------
        elif self.operador == OperadorAritmetico.UMENOS: #NEGACION UNARIA
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)


         #-----------------------INCREMENTO MAS MAS (++)----------------------------
        elif self.operador == OperadorAritmetico.MASMAS: #INCRMENTO ++
            print("INCREMENTO ENTRA")
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return  self.obtenerVal(self.OperacionIzq.tipo, izq)
            
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para INCREMENTO ++", self.fila, self.columna)   



        #-----------------------NEGACION BOOLEANA ----------------------------
        elif self.operador == OperadorLogico.NOT: #NEGACION UNARIA
            if self.OperacionIzq.tipo == TIPO.BOOLEANO:
                self.tipo = TIPO.BOOLEANO
                valorBool=self.obtenerVal(self.OperacionIzq.tipo, izq)
                if valorBool ==True:
                    valorBool==False
                elif valorBool ==False:
                    valorBool==True
                return valorBool
            
            return Excepcion("Semantico", "Tipo Erroneo de operacion para ! unario.", self.fila, self.columna)
        #CUALQUIER OTRO TIPO DE OPERACION    
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("ARITMETICA")
        if self.OperacionDer != None:
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionDer.getNodo())
        else:
            nodo.agregarHijo(str(self.operador))
            nodo.agregarHijoNodo(self.OperacionIzq.getNodo())

        return nodo 
        
    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        