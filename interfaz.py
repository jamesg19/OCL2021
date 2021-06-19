import os
import re
from TS.Excepcion import Excepcion
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from Instrucciones.Break import Break

#from tkinter import * as tk

raiz = tk.Tk()
global cont 
def salir(): #SALIR DEL PROGRAMA
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value :
        raiz.destroy()


archivo = ""
#FUNCIONALIDADES BASICA
# NUEVO DOCUMENTO
# ABRIR
# GUARDAR
# GUARDAR COMO
# SALIR DEL PROGRAMA
# EJECUTAR CODIGO
####################################################CREA UN NUEVO DOCUMENTO##########################################################
def nuevo():  
    global archivo
    editor.delete(1.0, tk.END)
    archivo = ""
######################################################ABRIR ARCHIVO#############################################################
def abrir():       
    global archivo
    archivo = tk.filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "")

    entrada = open(archivo)
    content = entrada.read()

    editor.delete(1.0, tk.END)
    for s in recorrerInput(content):
        editor.insert(tk.INSERT, s[1], s[0])
    entrada.close()
    lineas()
######################################################### ----GUARDAR---- #######################################################
def guardarArchivo():    
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(editor.get(1.0, tk.END))
        guardarc.close()

######################################################### GUARDAR COMO #######################################################
def guardarComo():      
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "")
    fguardar = open(guardar, "w+")
    fguardar.write(editor.get(1.0, tk.END))
    fguardar.close()
    archivo = guardar

def openPDF():      
    dirname = os.path.dirname(__file__)
    direcc = os.path.join(dirname, 'errores.pdf')
    os.startfile(direcc)
    
def pintar(*args):
    content = editor.get("1.0", tk.END)
    print(content)
    for s in recorrerInput(content):
        editor.insert(tk.INSERT, s[1], s[0])
    lineas()

##CONTADOR DE LINEAS EN LA BARRA VERTICAL
def lineas(*args):      #ACTUALIZAR LINEAS
    posicion(None)
    lines.delete("all")

    cont = editor.index("@1,0")
    
    while True :
        dline= editor.dlineinfo(cont)
        if dline is None: 
            break
        y = dline[1]
        strline = str(cont).split(".")[0]
        lines.create_text(2,y,anchor="nw", text=strline, font = ("Arial", 12))
        cont = editor.index("%s+1line" % cont)

def posicion(event):    #ACTUALIZAR POSICION
   #obtiene la posicion
    posicionCursor = "Cursor: "+editor.index(tk.INSERT)
    #settea el texto
    pos = ttk.Label( text = posicionCursor)    
    pos.config(text=str(posicionCursor).replace(".",","))
    #recorrerInput(editor.get(1,tk.END))
    pos.grid(column = 1, row = 4)

###########################################  METODO PARA EJECUTAR EL CODIGO  ##################################### 
def ejecutar():
    #f = open("./entradaa.txt", "r")
    #entrada = f.read()
    entrada = editor.get(1.0, tk.END)
    from TS.Arbol import Arbol
    from TS.TablaSimbolos import TablaSimbolos
    import grammar
    try:
        instrucciones = parse(entrada.lower()) #ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)
for error in errores:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
    ast.getExcepciones().append(error)
    ast.updateConsola(error.toString())

for instruccion in ast.getInstrucciones():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
    if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Excepcion) :
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString())
        if isinstance(value, Break): 
            err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
        
for instruccion in ast.getInstrucciones():      # 2DA PASADA (MAIN)
    contador = 0
    if isinstance(instruccion, Main):
        contador += 1
        if contador == 2: # VERIFICAR LA DUPLICIDAD
            err = Excepcion("Semantico", "Existen 2 funciones Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
            break
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Excepcion) :
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString())
        if isinstance(value, Break): 
            err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())

for instruccion in ast.getInstrucciones():    
    if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion)):
        err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
        ast.getExcepciones().append(err)
        ast.updateConsola(err.toString())

print(ast.getConsola())







    except IOError:
        print("a")
    print(ast.getConsola())  

#def debug():
    #btn = tk.Button(text="Next")
    #btn.grid(row=5, column = 0)
    
def search(re,txt):
    return not(txt == ' ' or txt == '\n' or  txt=='(' or txt == ')'or  txt=='{' or txt == '}' or txt=='"' or txt == "<" or txt == ">" or txt == "+" or txt == "-" or txt == "*" or txt == "/" or txt == "=" or txt == "!" or txt == "~" or txt == "%" or txt == "^" or txt == "|")


def recorrerInput(i):  #Funcion para obtener palabras reservadas, signos, numeros, etc

    lista = []
    val = ''
    counter = 0
    while counter < len(i):

        if re.search(r"[a-zA-Z0-9_]", i[counter]):#re.search(r"[a-z0-9]", i[counter])
            val += i[counter]
            print('valor ', val)
        elif re.search(r"[0-9]",i[counter]):
            l = []
            l.append("numero")
            l.append(i[counter])
            lista.append(l)

        elif re.search(r"\#",i[counter]):
            if i[counter + 1] == "*":
                while counter < len(i):
                    val += i[counter]
                    if i[counter] == "*" and i[counter+1]  == "\#":
                        print('valor if: ',val)
                        l = []
                        l.append("comentario")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    counter += 1
            else:
                print('comentario Simple')
                while counter < len(i):
                    print('counter: ',counter,' valor: ',i[counter])
                    val += i[counter]
                    if i[counter] == "\n" :
                        print('valor if: ',val)
                        l = []
                        l.append("comentario")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    counter += 1
        elif i[counter] == "$":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = "$"
        elif  i[counter] == "<" or i[counter] == ">" or i[counter] == "+" or i[counter] == "-" or i[counter] == "*" or i[counter] == "/" or i[counter] == "=" or i[counter] == "!" or i[counter] == "~" or i[counter] == "%" or i[counter] == "^" or i[counter] == "|":

            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            l = []
            l.append("operacion")
            l.append(i[counter])
            lista.append(l)
        elif i[counter] == "\"":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = i[counter]
            counter += 1
            while counter < len(i):
                if i[counter] == "\"":
                    val += i[counter]
                    l = []
                    l.append("string")
                    l.append(val)
                    lista.append(l)
                    val = ''
                    break
                val += i[counter]
                counter += 1
        elif i[counter] == "\'":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = i[counter]
            counter += 1
            while counter < len(i):
                if i[counter] == "\'":
                    val += i[counter]
                    l = []
                    l.append("string")
                    l.append(val)
                    lista.append(l)
                    val = ''
                    break
                val += i[counter]
                counter += 1
        else:
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            l = []
            l.append("signo")
            print('signo',i[counter])
            l.append(i[counter])
            lista.append(l)
        counter +=1

    for s in lista:
        txtIn=s[1].lower()
        if txtIn == 'var' or txtIn == 'false' or txtIn == 'true' or txtIn == 'int' or txtIn == 'float' or txtIn == 'char' or txtIn == 'print' or txtIn == 'main' or txtIn == 'goto' or txtIn == 'unset' or txtIn == 'exit' or txtIn == 'if' or txtIn == 'abs' or txtIn == 'xor' or txtIn == 'array' or txtIn == 'read':
            s[0] = 'reservada'
        elif s[1][0] != "$":
            if s[0] == 'variable':
                s[0] = 'etiqueta'
    return lista

########################################ELEMENTOS
frame   = tk.Frame(raiz, bg="gray60")
editor  = scrolledtext.ScrolledText( undo = True)
consola = scrolledtext.ScrolledText( undo = True)

#################################CAMBIO DE COLORES
editor.tag_config('reservada', foreground='blue')
editor.tag_config('string', foreground='orange')
editor.tag_config('numero', foreground='purple')
editor.tag_config('comentario', foreground='gray')

editor.tag_config('variable', foreground='maroon4')
editor.tag_config('operacion', foreground='red')
editor.tag_config('signo', foreground='black')

#####################FUNCIONALIDADES EN EL TECLADO
editor.config(bd=0, padx=6, pady=4, font=("Arial",12))
consola.config(bd=0,padx=6, pady=4, font=("Arial",12),height=10)
#Barra vertical, izquierda, donde se mostrara la catidad de lineas
lines = tk.Canvas( width = 30, height = 465, background = 'gray60')
lbl = ttk.Label( text = "Salida:")    

editor.bind('<Return>',    lineas)
editor.bind('<BackSpace>', lineas)
editor.bind('<<Change>>',  lineas)
editor.bind('<Configure>', lineas)
#editor.bind('<Motion>', lineas)
editor.bind('<KeyPress>', lineas)
editor.bind('<Button-1>', posicion)

frame.grid(sticky='news')

#Posicion de los elementos
editor.grid (row = 3, column = 1, padx = 10,  pady = 10)
consola.grid(row = 5, column = 1, padx = 10,  pady = 10)
lines.grid  (row = 3, column = 0 )
lbl.grid(row=4,column=0)

#menu
menubar  = tk.Menu(raiz)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo",   command=nuevo)
filemenu.add_command(label="Abrir",   command=abrir)
filemenu.add_command(label="Guardar", command=guardarArchivo)
filemenu.add_command(label="Guardar como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir",   command=salir)

menubar.add_cascade(menu=filemenu, label="Archivo")

run = tk.Menu(menubar,tearoff=0)

run.add_command(label="Ejecutar", command=ejecutar)
menubar.add_cascade(menu=run, label="Ejecutar")


raiz.title("COMPI 1 2021 JAMES GRAMAJO")
raiz.config(menu=menubar)

#from grammar import compilar as exec_code

def  imprimir_en_consola(consol):
    consola.delete("1.0",tk.END)
    consola.insert(tk.INSERT,consol)
raiz.mainloop()