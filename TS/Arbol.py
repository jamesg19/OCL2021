class Arbol:
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = ""
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
        self.consola += str(cadena) + '\n'

    def updateConsolaError(self,cadena):
        self.consolaError+=str(cadena)+ '\n'

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal