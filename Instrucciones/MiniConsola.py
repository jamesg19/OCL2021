
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
import tkinter as tk
from tkinter import simpledialog

class MiniConsola():
    
    # the input dialog
    def __init__(self):
        pass
        


    def getValor(self):
        ROOT = tk.Tk()

        ROOT.withdraw()
        self.USER_INP = simpledialog.askstring(title="Consola JPR",prompt="Ingresa en consola:")
        print(self.USER_INP)
        return self.USER_INP
    



    def close_window (root): 
        root.destroy()

    # check it out
    #print("Hello", self.USER_INP)