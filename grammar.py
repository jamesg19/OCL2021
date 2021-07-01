'''
ESCUELA DE VACACIONES JUNIO 2021 USAC
GRAMATICA PROYECTO COMPILADORES 1 
ALUMNO: JAMES OSMIN GRAMAJO CARCAMO
CARNÉ: 3517 27817 0922 (DPI)
ESTUDIANTE EXTERNO (CUNOC-QUETZALTENANGO)
'''

from Expresiones.AccesoArreglo import AccesoArreglo
from Instrucciones.DeclaracionArr1 import DeclaracionArr1
from Instrucciones.ModificarArreglo import ModificarArreglo
import re
from TS.Excepcion import Excepcion
#TABLA ASCII 
#https://es.stackoverflow.com/questions/117556/clase-de-caracteres-para-cualquier-letra-incluyendo-todo-tipo-de-acentos
errores = []
reservadas = {
    'var'           : 'VAR',
    'true'          : 'TRUE',
    'false'         : 'FALSE',
    'null'          : 'NULL',
    'int'           : 'INT',
    'double'        : 'DOUBLE',
    'string'        : 'STRING',
    'char'          : 'CHAR',
    'boolean'       : 'BOOLEAN',
    'new'           : 'NEW',
    'else'          : 'ELSE',
    'print'         : 'PRINT',
    'switch'        : 'SWITCH',
    'case'          : 'CASE',
    'default'       : 'DEFAULT',
    'break'         : 'BREAK',
    'while'         : 'WHILE',
    'for'           : 'FOR',
    'return'        : 'RETURN',
    'func'          : 'FUNC',
    'main'          : 'MAIN',
    'if'            : 'IF',
    'read'          : 'READ',
    'tolower'       : 'TOLOWER',
    'toupper'       : 'TOUPPER',
    'truncate'      : 'TRUNCATE',
    'round'         : 'ROUND',
    'typeof'        : 'TYPEOF',
    'lenght'        : 'LENGHT',
    'func'          : 'FUNC',
    'continue'      : 'CONTINUE',

}





tokens=[

    'ESPBARRAINVERTIVA',
    'ESPLINEA',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POT',
    'MODULO',
    'IGUAL',
    'IGUALACION',
    'DECIMAL',
    'ENTERO',
    'CHART',
    'DIREFENCIACION',
    'MENORQ',
    'MAYORQ',
    'MENORIGUAL',
    'MAYORIGUAL',
    ##OPERADOR LOGICO
    'OR',
    'AND',
    'NOT',
    #ENCAPSULACION
    'PTCOMA',
    'COMA',
    'DOSPUNTOS',
    'CORCHETE_ABRE',
    'CORCHETE_CIERRA',
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    'PARENTESIS_ABRE',
    'PARENTESIS_CIERRA',

    #INCREMENTO Y DECREMENTO
    'INCREMENTO',
    'DECREMENTO',
    'IDENTIFICADOR',
    'CADENA'
]+ list(reservadas.values())
states = (
  ('COMENTARIOBLOQU','exclusive'),
)

#tokens

t_ESPBARRAINVERTIVA=r'[\\]'
t_ESPLINEA=         r'[\\][n]'
t_MAS=              r'\+'
t_MENOS=            r'-'
t_POR=              r'\*'
t_DIV=              r'/'
t_POT=              r'\*\*'
t_MODULO=           r'\%'
#OPERADORES RELACIONALES
t_IGUAL=            r'='
t_IGUALACION=       r'[=][=]'
t_DIREFENCIACION=   r'=!'
t_MENORQ=           r'<'
t_MAYORQ=           r'>'
t_MENORIGUAL=       r'<='
t_MAYORIGUAL=       r'>='
#OPERADOR LOGICO
t_AND=              r'&&'
t_OR=               r'\|\|'
t_NOT=              r'!'
#ENCAPSULACION
t_PTCOMA=           r';'
t_COMA=             r','
t_DOSPUNTOS=        r':'
t_CORCHETE_ABRE=    r'\['
t_CORCHETE_CIERRA=  r'\]'
t_LLAVE_ABRE=       r'\{'
t_LLAVE_CIERRA=     r'\}'
t_PARENTESIS_ABRE=  r'\('
t_PARENTESIS_CIERRA=r'\)'
t_INCREMENTO=       r'\+\+'
t_DECREMENTO=       r'\-\-'
#t_IDENTIFICADOR=    r'[A-Z_-z0-9]+'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es demasiado grande '%d'" % t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large '%d'" % t.value)
        t.value = 0
    return t
def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(),'IDENTIFICADOR')
    return t


def t_begin_COMENTARIOBLOQU(t):
    r'[\#][\*]'
    print('entra')
    t.lexer.begin('COMENTARIOBLOQU')             # Starts 'COMENTARIOBLOQU' state

def t_COMENTARIOBLOQU_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIOBLOQU_LETRAS(t):
    r'[^\*\#]'
    return None

def t_COMENTARIOBLOQU_end(t):
    r'\*\#'
    print('sale')
    t.lexer.begin('INITIAL')

def t_COMENTARIO(t):
    r'[\#][^\n]+'
    print('Comment Line')
    return None

def t_CADENA(t):
    r'(\"([(-Za-zÀ-ÖØ-öø-ÿ#-&]|([\\][nN]|[\\][tT]|[\\][rR]|[\\][\']|[\\][\"]|[\\][\\]|[\{]|[\}]|[\|]|[\!]|[\_]|[]|[ ]|[░░]|[▒▒]|[▓▓]|[@]|[\^]))*\")'
    t.value = t.value[1:-1] # remuevo las comillas
    #t.value.replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t').replace('\\"', '\"').replace('\\\\', '\\')
    return t

def t_CHART(t):
    r'(\'([(-Za-zÀ-ÖØ-öø-ÿ#-&]|([\\][nN]|[\\][tT]|[\\][rR]|[\\][\']|[\\][\"]|[\\][\\]|[\{]|[\}]|[\|]|[\!]|[\_]|[]|[ ]))\')'
    #r'(\'([(-Za-z#-&]|([\\n]|[\\t]|[\\r]|[\\][\\]|[\\][\']|[\\][\"]|[\{]|[\}]|[\|]|[\!]|[\_]|[]|[ ]))\')'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

# Caracteres ignorados
t_ignore = " \t"
t_COMENTARIOBLOQU_ignore = "\r\t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIOBLOQU_error(t): #LEXICOS
    #print('caracter no reconocido  ' + str(t.value[0]))
    # almacenamiento de errores lexicos
    t.lexer.skip(1)

def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)


# Presedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOTT'),
    ('left', 'IGUALACION', 'DIREFENCIACION', 'MENORQ', 'MENORIGUAL', 'MAYORQ', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIV', 'POR','MODULO'),
    ('left', 'POT'),
    ('left', 'MASMAS','MENOSMENOS'),
    ('right', 'UMENOS')
)


# Definición de la gramática

#Abstract
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, OperadorLogico, TIPO, OperadorRelacional
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.For import For
from Instrucciones.ForA import ForA
from Instrucciones.Switch import Switch
from Instrucciones.Case import Case
from Instrucciones.Break import Break
from Instrucciones.Default import Default
from Instrucciones.Main import Main
from Instrucciones.DeclaracionNULA import DeclaracionNULA
from Instrucciones.AsignacionNULA import AsignacionNULA
from Expresiones.Incremento import Incremento
from Expresiones.Decremento import Decremento
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Nativas.Truncate import Truncate
from Nativas.ToLower import ToLower
from Nativas.ToUpper import ToUpper
from Nativas.Round import Round
from Nativas.Typeof import Typeof
from Instrucciones.Return import Return
from Nativas.Lenght import Lenght
from Expresiones.Casteo import Casteo
from Instrucciones.Continue import Continue


def p_inicio(t):
    'init : instrucciones'
    t[0] = t[1]

def p_main(t):
    ''' instrucciones : instrucciones instruccion '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    :  instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

def p_declaraciones(t):
    '''
    instruccion : variables
                | if
                | switch
                | while
                | for
                | print
                | break
                | continue
                | returnn finInstruccion
                | main
                | funcion_void
                | llamada_fvoid finInstruccion
                | declArr_instr finInstruccion
                | modArr_instr finInstruccion
                
    '''
    t[0] = t[1]
def p_instruccion_error(t):
    'instruccion : error PTCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_variables1(t):
    ''' variables : var IDENTIFICADOR finInstruccion '''
    t[0] = DeclaracionNULA(TIPO.NULO, t[2], t.lineno(2), find_column(input, t.slice[2]))
def p_declara(t):
    ''' variables : var IDENTIFICADOR  IGUAL expresion  finInstruccion ''' 
    t[0] = Declaracion(TIPO.ENTERO, t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
    
def p_asginacionnula1(t):
    ''' variables : var IDENTIFICADOR  IGUAL NULL  finInstruccion '''
    t[0] = DeclaracionNULA(TIPO.NULO, t[2], t.lineno(2), find_column(input, t.slice[2]))

def p_asgina(t):
    ''' variables : IDENTIFICADOR IGUAL expresion finInstruccion ''' 
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_asginacionnula2(t):
    ''' variables : IDENTIFICADOR  IGUAL NULL  finInstruccion '''
    t[0] = AsignacionNULA(t[1], None, t.lineno(1), find_column(input, t.slice[1]))

def p_var(t):
    ''' var : VAR '''
    #--------------------INCREMENTO Y DECREMENTO
def p_incrementa(t):
    ''' variables : IDENTIFICADOR INCREMENTO finInstruccion ''' 
    t[0] = Incremento(t[1], t.lineno(1), find_column(input, t.slice[1]))
    
def p_decrementa(t):
    ''' variables : IDENTIFICADOR DECREMENTO finInstruccion ''' 
    t[0] = Decremento(t[1], t.lineno(1), find_column(input, t.slice[1]))

#--------------------------IF------------------------
def p_if1(t):
    '''
    if : IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA  
    '''
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_ifelse(t):
    ''' if : IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE LLAVE_ABRE instrucciones LLAVE_CIERRA
    '''
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_difelseif(t):
    ''' if :  IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE if '''
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))



def p_switch(t):
    ''' switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases LLAVE_CIERRA '''
    t[0] = Switch(t[3],t[6],None,t.lineno(5), find_column(input, t.slice[5]))

def p_switch1(t):
    ''' switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases default LLAVE_CIERRA '''
    t[0] = Switch(t[3], t[6], t[7], t.lineno(5), find_column(input, t.slice[5]))
    
def p_switch2(t):
    ''' switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE  default LLAVE_CIERRA '''
    t[0] = Switch(t[3], None, t[6], t.lineno(5), find_column(input, t.slice[5]))
    
def p_listacases1(t):
    ''' listacases : listacases case '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

def p_listacases2(t):
    ''' listacases :  case '''
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

def p_cases(t):
    ''' case : CASE expresion DOSPUNTOS instrucciones '''
    t[0] = Case(t[2],t[4],t.lineno(3), find_column(input, t.slice[3]))

def p_defauult(t):
    ''' default : DEFAULT DOSPUNTOS instrucciones '''
    t[0] = Default(t[3],t.lineno(2), find_column(input, t.slice[2]))


def p_menu(t):
    ''' main : MAIN PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA '''
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))

def p_while(t):
    ''' while : WHILE PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA '''
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))
def p_for1(t):
    ''' for : FOR PARENTESIS_ABRE declaracionfor1 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA  LLAVE_ABRE instrucciones LLAVE_CIERRA
    '''
    t[0]=For(t[3],t[5],t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))

def p_for2(t):
    ''' for : FOR PARENTESIS_ABRE declaracionfor2 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA  LLAVE_ABRE instrucciones LLAVE_CIERRA
    '''
    t[0]=ForA(t[3],t[5],t[7],t[10],t.lineno(1), find_column(input, t.slice[1]))


def p_declaracionfor1(t):
    ''' declaracionfor1 : VAR IDENTIFICADOR IGUAL expresion   '''
    t[0] = Declaracion(TIPO.ENTERO, t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

def p_declaracionfor2(t):
    ''' declaracionfor2 : IDENTIFICADOR IGUAL expresion  '''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_actualizacionfor1(t):
    ''' actualizacion : IDENTIFICADOR INCREMENTO '''
    t[0] = Incremento(t[1], t.lineno(1), find_column(input, t.slice[1]))
def p_actualizacionfor2(t):
    ''' actualizacion :  IDENTIFICADOR DECREMENTO '''
    t[0] = Decremento(t[1], t.lineno(1), find_column(input, t.slice[1]))
def p_actualizacionfor3(t):
    ''' actualizacion :   IDENTIFICADOR IGUAL expresion '''
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))
##########################################  FUNCIONES ########################################
def p_llamada1(t) :
    ''' llamada_fvoid     : IDENTIFICADOR PARENTESIS_ABRE  PARENTESIS_CIERRA '''
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))

def p_llamada2(t) :
    ''' llamada_fvoid     : IDENTIFICADOR PARENTESIS_ABRE parametros_llamada PARENTESIS_CIERRA '''
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////DECLARACION ARREGLOS//////////////////////////////////////////////////

def p_declArr(t) :
    '''declArr_instr     : tipo1'''
    t[0] = t[1]

def p_tipo1(t) :
    '''tipo1     : tip lista_Dimension IDENTIFICADOR IGUAL NEW tip lista_expresiones'''
    t[0] = DeclaracionArr1(t[1], t[2], t[3], t[6], t[7], t.lineno(3), find_column(input, t.slice[3]))

def p_lista_Dim1(t) :
    '''lista_Dimension     : lista_Dimension CORCHETE_ABRE CORCHETE_CIERRA'''
    t[0] = t[1] + 1

def p_lista_Dim2(t) :
    'lista_Dimension    : CORCHETE_ABRE CORCHETE_CIERRA'
    t[0] = 1

def p_lista_expresiones_1(t) :
    'lista_expresiones     : lista_expresiones CORCHETE_ABRE expresion CORCHETE_CIERRA'
    t[1].append(t[3])
    t[0] = t[1]

def p_lista_expresiones_2(t) :
    'lista_expresiones    : CORCHETE_ABRE expresion CORCHETE_CIERRA'
    t[0] = [t[2]]

def p_tip(t):
    ''' tip : STRING
            | INT
            | DOUBLE 
            | CHAR
            | BOOLEAN'''
    if t[1].lower()=="string":
        t[0]=TIPO.CADENA
    elif t[1].lower()=="int":
        t[0]=TIPO.ENTERO
    elif t[1].lower()=="double":
        t[0]=TIPO.DECIMAL
    elif t[1].lower()=="char":
        t[0]=TIPO.CHARACTER
    elif t[1].lower()=="boolean":
        t[0]=TIPO.BOOLEANO

#///////////////////////////////////////////  MODIFICACION ARREGLOS  ///////////////////////////////////////////////


def p_modArr(t) :
    '''modArr_instr     :  IDENTIFICADOR lista_expresiones IGUAL expresion'''
    t[0] = ModificarArreglo(t[1], t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////////// RETURN /////////////////////////////////////////////////////////

def p_returnn(t):
    ''' returnn : RETURN expresion '''
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))
    
def p_parametros1(t) :
    'parametros_llamada : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros2(t) :
    'parametros_llamada : parametro_llamada'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t) :
    'parametro_llamada : expresion'
    t[0] = t[1]

def p_funcion_void(t):
    ''' funcion_void : FUNC IDENTIFICADOR PARENTESIS_ABRE  PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA
    '''
    t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_void2(t):
    ''' funcion_void : FUNC IDENTIFICADOR PARENTESIS_ABRE parametros PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA '''
    t[0] = Funcion(t[2],t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS 1+//////////////////////////////////////////////////

def p_parametros_1(t) :
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]

def p_parametros_2(t) :
    'parametros    : parametro'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO 1 //////////////////////////////////////////////////

def p_parametro_int(t) :
    'parametro     : INT IDENTIFICADOR'
    t[0] = {'tipo':TIPO.ENTERO,'identificador':t[2]}

def p_parametro_string(t) :
    'parametro     : STRING IDENTIFICADOR'
    t[0] = {'tipo':TIPO.CADENA,'identificador':t[2]}

def p_parametro_decimal(t) :
    'parametro     : DOUBLE IDENTIFICADOR'
    t[0] = {'tipo':TIPO.DECIMAL,'identificador':t[2]}

def p_parametro_boolean(t) :
    'parametro     : BOOLEAN IDENTIFICADOR'
    t[0] = {'tipo':TIPO.BOOLEANO,'identificador':t[2]}

def p_parametro_char(t) :
    'parametro     : CHAR IDENTIFICADOR'
    t[0] = {'tipo':TIPO.CHARACTER,'identificador':t[2]}


def p_print(t):
    ''' print : PRINT PARENTESIS_ABRE expresion PARENTESIS_CIERRA finInstruccion '''
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_break(t):
    ''' break : BREAK finInstruccion '''
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

def p_continue(t):
    ''' continue : CONTINUE finInstruccion '''
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

def p_finInstruccion(t):
    ''' finInstruccion : PTCOMA
                    | '''
    t[0] = None

def p_expresion_binaria(t):
    ''' expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POT  expresion
            | expresion MODULO expresion
            | expresion IGUALACION expresion
            | expresion DIREFENCIACION expresion
            | expresion MAYORQ expresion
            | expresion MENORQ expresion
            | expresion MAYORIGUAL expresion
            | expresion MENORIGUAL expresion  
            | expresion OR expresion  
            | expresion AND expresion 
    ''' 
    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1],t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''
    expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec NOTT
    '''
    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2],None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2],None, t.lineno(1), find_column(input, t.slice[1]))

def p_incremento(t):
    ''' expresion : IDENTIFICADOR INCREMENTO %prec MASMAS'''
    t[0] = Incremento(t[1], t.lineno(1), find_column(input, t.slice[1]))
    

def p_decremento(t):
    ''' expresion : IDENTIFICADOR DECREMENTO %prec MENOSMENOS '''
    t[0] = Decremento(t[1], t.lineno(1), find_column(input, t.slice[1]))


def p_expresion_agrupacionn(t):
    '''
    expresion : PARENTESIS_ABRE expresion PARENTESIS_CIERRA
    '''
    t[0] = t[2]
def p_entero(t):
    ''' expresion : ENTERO '''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))
def p_decimal(t):
    ''' expresion : DECIMAL '''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))
def p_true(t):
    ''' expresion : TRUE '''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))
def p_false(t):
    ''' expresion : FALSE '''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))
def p_identificador(t):
    ''' expresion : IDENTIFICADOR '''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))
def p_cadena(t):
    ''' expresion : CADENA '''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t').replace('\\"', '\"').replace('\\\\', '\\').replace('\\\'', '\''), t.lineno(1), find_column(input, t.slice[1]))
def p_chart(t):
    ''' expresion : CHART '''
    t[0] = Primitivos(TIPO.CHARACTER,str(t[1]).replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t').replace('\\"', '\"').replace('\\\\', '\\').replace('\\\'', '\''), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_llamadaa(t):
    '''expresion : llamada_fvoid '''
    t[0] = t[1]

def p_toupper(t):
    ''' expresion : TOUPPER PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = ToUpper(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_tolower(t):
    ''' expresion : TOLOWER PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = ToLower(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_truncate(t):
    ''' expresion : TRUNCATE PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = Truncate(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_round(t):
    ''' expresion : ROUND PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = Round(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_typeof(t):
    ''' expresion : TYPEOF PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = Typeof(t[3], t.lineno(1), find_column(input, t.slice[1]))
def p_lenght(t):
    ''' expresion : LENGHT PARENTESIS_ABRE expresion PARENTESIS_CIERRA '''
    t[0] = Lenght(t[3], t.lineno(1), find_column(input, t.slice[1]))
#*************************************************************CASTEOS************************************************************
def p_castINT(t):
    ''' expresion : PARENTESIS_ABRE INT PARENTESIS_CIERRA expresion '''
    t[0] = Casteo(TIPO.ENTERO, t[4], t.lineno(2), find_column(input, t.slice[2]))
def p_castDOUBLE(t):
    ''' expresion : PARENTESIS_ABRE DOUBLE PARENTESIS_CIERRA expresion '''
    t[0] = Casteo(TIPO.DECIMAL, t[4], t.lineno(2), find_column(input, t.slice[2]))
def p_castSTRING(t):
    ''' expresion : PARENTESIS_ABRE STRING PARENTESIS_CIERRA expresion '''
    t[0] = Casteo(TIPO.CADENA, t[4], t.lineno(2), find_column(input, t.slice[2]))
def p_castBOOLEAN(t):
    ''' expresion : PARENTESIS_ABRE BOOLEAN PARENTESIS_CIERRA expresion '''
    t[0] = Casteo(TIPO.BOOLEANO, t[4], t.lineno(2), find_column(input, t.slice[2]))
def p_castCHAR(t):
    ''' expresion : PARENTESIS_ABRE CHAR PARENTESIS_CIERRA expresion '''
    t[0] = Casteo(TIPO.CHARACTER, t[4], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_Arreglo(t):
    '''expresion : IDENTIFICADOR lista_expresiones'''
    t[0] = AccesoArreglo(t[1], t[2], t.lineno(1), find_column(input, t.slice[1]))

'''
import ply.yacc as yacc
parser = yacc.yacc()
f = open("./entradaa.txt", "r")
input = f.read()
#print(input)
parser.parse(input)
print("Archivo ejecutado correctamente :D")
'''

import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)


#-------------------------------------------------INTERFAZ-------------------------------------------------
'''
f = open("./entradaa.txt", "r",encoding="utf-8")
entrada = f.read()
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
try:
    instrucciones = parse(entrada.lower()) #ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    for error in errores:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())
    for instruccion in ast.getInstrucciones():      # 1ERA PASADA (DECLARACIONES Y ASIGNACIONES)
        if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, DeclaracionNULA) or isinstance(instruccion, AsignacionNULA):
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
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, DeclaracionNULA)  or isinstance(instruccion, Asignacion)  or isinstance(instruccion, AsignacionNULA)):
            err = Excepcion("Semantico", "Sentencias fuera de Main", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
except:
    print("a")
print(ast.getConsola())
'''