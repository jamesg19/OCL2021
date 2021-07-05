import tkinter
class Arbol:
    def __init__(self, instrucciones , consolaJPR):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.funciones=[]
        self.consola = ""
        self.consolaJPR=consolaJPR
        self.consolaError=""
        self.TSglobal = None

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola

    def getConsolaError(self):
        return self.consolaError
    
    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self,cadena):
        self.consolaJPR.insert(tkinter.INSERT,str(cadena)+"\n")
        #self.consola += str(cadena) + '\n'

    def updateConsolaError(self,cadena):
        
        self.consolaError+=str(cadena)+ '\n'

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal
        
    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getDot(self, raiz): ## DEVUELVE EL STRING DE LA GRAFICA EN GRAPHVIZ
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)