import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 200)
canvas1.pack()
y1="aasdfdasd"
label1 = tk.Label(root, text= "Hola Mundo")
canvas1.create_window(150, 50, window=label1)

entry1 = tk.Entry (root) 
canvas1.create_window(150, 80, window=entry1)
class consolajpr:
    def __init__(self):
        self.lectura=""

    def Ingresar():  
        x1 = entry1.get()
        #self.lectura=x1
        #print(x1)

    def getTextoConsola(self):
        return self.lectura



    button1 = tk.Button(text='Ingresar', command=Ingresar)
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()