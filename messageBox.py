from tkinter import *
import sys

class popupWindow(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Ingrese un valor:")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Limpiar',command=self.clean)
        self.b.pack()
        self.b=Button(top,text='Ok',command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()
    def clean(self):
        
        self.value=""


class mainWindow(object):
    def __init__(self,master):
        #top=self.top=Toplevel(master)
        self.master=master
        self.b=Button(master,text="Click me!...",command=self.popup)
        self.b.pack()
        self.b=Entry(master)
        self.b2=Button(master,text="print value",command=lambda: sys.stdout.write(self.entryValue()+'\n'))
        self.b2.pack()

    def popup(self):
        self.w=popupWindow(self.master)
        self.b["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.b["state"] = "normal"

    def entryValue(self):
        return self.w.value


if __name__ == "__main__":
    root=Tk()
    m=mainWindow(root)
    root.mainloop()