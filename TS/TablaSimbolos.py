from TS.Excepcion import Excepcion
from TS.Tipo import  TIPO
variables=[]
class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        self.entorno="GLOBAL"
        #self.funciones = []

    def setTabla(self, simbolo):      # Agregar una variable
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            ##
            encontro=True
            if len(variables)>0:
                for variable in variables:
                    if variable.id==simbolo.id:
                        encontro=True
                        break
                    else:
                        encontro=False
                if encontro==False:
                    variables.append(simbolo)
            else:
                variables.append(simbolo)

            ##


            return None

    def getTabla(self, id):            # obtener una variable
        try:
            tablaActual = self
            while tablaActual.tabla != None:
                if id.lower() in tablaActual.tabla :
                    return tablaActual.tabla[id.lower()]           # RETORNA SIMBOLO
                else:
                    tablaActual = tablaActual.anterior
        except:
            return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id.lower()].getTipo()==TIPO.NULO or simbolo.getTipo()==TIPO.NULO :
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    try:
                        pass
                        #for variable in variables:
                            #if variable.id==simbolo.id:
                                #variable.setValor(simbolo.getValor())
                                #variable.setTipo(tablaActual.tabla[simbolo.id.lower()].getTipo())
                                #break 
                    except:
                        pass
                    return None             #VARIABLE ACTUALIZADA
                
                return Excepcion("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.anterior
        
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())
        




    #TABLA DE SIMBOLOS ES PARA VARIABLES
    def getEntorno(self):
        return self.entorno

    def setEntorno(self,entorno):
        self.entorno=entorno

    def getVariables(self):
        return variables
        
    def tsvariables(self):
        global variables
        variables=[]