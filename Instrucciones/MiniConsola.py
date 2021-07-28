from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO
import tkinter as tk
from tkinter import simpledialog


class MiniConsola():


    # the input dialog
    def __init__(self, titulo,root):
        #ROOT = tk.Tk()
        #ROOT.withdraw()
        self.titulo = titulo
        self.root=root
        pass

    def getValor(self):

        self.USER_INP = simpledialog.askstring(title=self.titulo, prompt="Ingresa en consola:",parent=self.root)

        print(self.USER_INP)

        # Mostrar nuevamente la ventana principal
        self.root.deiconify()
        return self.USER_INP

    def close_window(root):
        root.destroy()


