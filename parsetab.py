
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTTleftIGUALACIONDIREFENCIACIONMENORQMENORIGUALMAYORQMAYORIGUALleftMASMENOSleftDIVPORMODULOleftPOTleftMASMASMENOSMENOSrightUMENOSAND BREAK CADENA CASE CHAR CHART COMA COMILLAS COMILLASIMPLE CORCHETE_ABRE CORCHETE_CIERRA DECIMAL DECREMENTO DEFAULT DIREFENCIACION DIV DOSPUNTOS DOUBLE ELSE ENTERO ESPBARRAINVERTIVA ESPCOMILLAS ESPCOMILLASIMPLE ESPLINEA ESPRETORNO ESPTAB FALSE FOR FUNC IDENTIFICADOR IF IGUAL IGUALACION INCREMENTO INT LLAVE_ABRE LLAVE_CIERRA MAIN MAS MAYORIGUAL MAYORQ MENORIGUAL MENORQ MENOS MODULO NEW NOT NULL OR PARENTESIS_ABRE PARENTESIS_CIERRA POR POT PRINT PTCOMA READ RETURN STRING SWITCH TOLOWER TOUPPER TRUE VAR WHILEinit : instrucciones instrucciones : instrucciones instruccion instrucciones    :  instruccion\n    instruccion : variables\n                | if\n                | switch\n                | while\n                | for\n                | funciones \n                | print\n                | break\n                | main\n                | funcion_void\n                | llamada_fvoid\n    instruccion : error PTCOMA variables : var IDENTIFICADOR finInstruccion  variables : var IDENTIFICADOR  IGUAL expresion  finInstruccion  variables : var IDENTIFICADOR  IGUAL NULL  finInstruccion  variables : IDENTIFICADOR IGUAL expresion finInstruccion  variables : IDENTIFICADOR  IGUAL NULL  finInstruccion  var : VAR  variables : IDENTIFICADOR INCREMENTO finInstruccion  variables : IDENTIFICADOR DECREMENTO finInstruccion \n    if : IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA  \n     if : IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE LLAVE_ABRE instrucciones LLAVE_CIERRA\n     if :  IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE if  switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases LLAVE_CIERRA  switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases default LLAVE_CIERRA  switch : SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE  default LLAVE_CIERRA  listacases : listacases case  listacases :  case  case : CASE expresion DOSPUNTOS instrucciones  default : DEFAULT DOSPUNTOS instrucciones  main : MAIN PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA  while : WHILE PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA  for : FOR PARENTESIS_ABRE declaracionfor1 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA  LLAVE_ABRE instrucciones LLAVE_CIERRA\n     for : FOR PARENTESIS_ABRE declaracionfor2 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA  LLAVE_ABRE instrucciones LLAVE_CIERRA\n     declaracionfor1 : VAR IDENTIFICADOR IGUAL expresion    declaracionfor2 : IDENTIFICADOR IGUAL expresion   actualizacion : IDENTIFICADOR INCREMENTO  actualizacion :  IDENTIFICADOR DECREMENTO  actualizacion :   IDENTIFICADOR IGUAL expresion  llamada_fvoid     : IDENTIFICADOR PARENTESIS_ABRE  PARENTESIS_CIERRA finInstruccion funcion_void : FUNC IDENTIFICADOR PARENTESIS_ABRE  PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA\n    \n    funciones : FUNC IDENTIFICADOR PARENTESIS_ABRE parametrosf PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA\n    \n    parametrosf : STRING IDENTIFICADOR COMA parametrosf\n                | STRING IDENTIFICADOR \n                | INT IDENTIFICADOR COMA parametrosf\n                | INT IDENTIFICADOR\n                | CHAR IDENTIFICADOR COMA parametrosf\n                | CHAR IDENTIFICADOR\n                | DOUBLE IDENTIFICADOR COMA parametrosf\n                | DOUBLE IDENTIFICADOR\n     print : PRINT PARENTESIS_ABRE expresion PARENTESIS_CIERRA finInstruccion  break : BREAK finInstruccion  finInstruccion : PTCOMA\n                    |  expresion : expresion MAS expresion\n            | expresion MENOS expresion\n            | expresion POR expresion\n            | expresion DIV expresion\n            | expresion POT  expresion\n            | expresion MODULO expresion\n            | expresion IGUALACION expresion\n            | expresion DIREFENCIACION expresion\n            | expresion MAYORQ expresion\n            | expresion MENORQ expresion\n            | expresion MAYORIGUAL expresion\n            | expresion MENORIGUAL expresion  \n            | expresion OR expresion  \n            | expresion AND expresion \n    \n    expresion : MENOS expresion %prec UMENOS\n                | NOT expresion %prec NOTT\n     expresion : IDENTIFICADOR INCREMENTO %prec MASMAS expresion : IDENTIFICADOR DECREMENTO %prec MENOSMENOS \n    expresion : PARENTESIS_ABRE expresion PARENTESIS_CIERRA\n     expresion : ENTERO  expresion : DECIMAL  expresion : TRUE  expresion : FALSE  expresion : IDENTIFICADOR  expresion : CADENA  expresion : CHART '
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,15,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,15,15,15,-54,15,15,15,15,-34,-24,-27,-29,15,-35,-45,-44,-28,15,15,15,-26,15,15,15,15,15,15,-25,-36,-37,]),'IDENTIFICADOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,16,22,24,26,27,28,29,30,31,32,34,35,36,37,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,65,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,97,98,100,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,131,134,139,140,141,146,147,148,149,152,157,158,159,162,163,165,169,170,176,177,178,182,184,185,186,187,189,190,191,192,193,194,195,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,29,38,-57,-21,-2,-15,-57,45,-57,-57,45,45,45,66,45,-55,-56,-16,45,-81,-57,-57,45,45,45,-77,-78,-79,-80,-82,-83,-22,-23,-57,99,-57,-57,-74,-75,-19,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-20,-72,-73,-43,45,45,45,135,136,137,138,-57,17,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,17,17,45,17,-54,17,17,45,17,167,167,17,-34,-24,-27,-29,17,-35,-45,-44,-28,17,17,45,17,-26,17,17,17,17,17,17,-25,-36,-37,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,175,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,18,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,18,18,18,-54,18,18,18,18,-34,-24,-27,-29,18,-35,-45,-44,18,-28,18,18,18,-26,18,18,18,18,18,18,-25,-36,-37,]),'SWITCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,19,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,19,19,19,-54,19,19,19,19,-34,-24,-27,-29,19,-35,-45,-44,-28,19,19,19,-26,19,19,19,19,19,19,-25,-36,-37,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,20,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,20,20,20,-54,20,20,20,20,-34,-24,-27,-29,20,-35,-45,-44,-28,20,20,20,-26,20,20,20,20,20,20,-25,-36,-37,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,21,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,21,21,21,-54,21,21,21,21,-34,-24,-27,-29,21,-35,-45,-44,-28,21,21,21,-26,21,21,21,21,21,21,-25,-36,-37,]),'FUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,22,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,22,22,22,-54,22,22,22,22,-34,-24,-27,-29,22,-35,-45,-44,-28,22,22,22,-26,22,22,22,22,22,22,-25,-36,-37,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,23,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,23,23,23,-54,23,23,23,23,-34,-24,-27,-29,23,-35,-45,-44,-28,23,23,23,-26,23,23,23,23,23,23,-25,-36,-37,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,24,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,24,24,24,-54,24,24,24,24,-34,-24,-27,-29,24,-35,-45,-44,-28,24,24,24,-26,24,24,24,24,24,24,-25,-36,-37,]),'MAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,25,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,25,25,25,-54,25,25,25,25,-34,-24,-27,-29,25,-35,-45,-44,-28,25,25,25,-26,25,25,25,25,25,25,-25,-36,-37,]),'VAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,37,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,134,139,140,141,147,152,157,158,159,162,163,165,169,170,176,177,178,184,185,186,187,189,190,191,192,193,194,195,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,65,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,26,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,26,26,26,-54,26,26,26,26,-34,-24,-27,-29,26,-35,-45,-44,-28,26,26,26,-26,26,26,26,26,26,26,-25,-36,-37,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,139,157,158,159,162,165,169,170,176,185,193,194,195,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,-54,-34,-24,-27,-29,-35,-45,-44,-28,-26,-25,-36,-37,]),'LLAVE_CIERRA':([3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,139,140,141,142,143,144,147,151,152,157,158,159,160,161,162,165,169,170,176,177,185,186,190,191,192,193,194,195,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,-54,157,158,159,162,-31,165,169,170,-34,-24,-27,176,-30,-29,-35,-45,-44,-28,-33,-26,-32,193,194,195,-25,-36,-37,]),'DEFAULT':([3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,139,142,144,157,158,159,161,162,165,169,170,176,185,186,193,194,195,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,145,-54,145,-31,-34,-24,-27,-30,-29,-35,-45,-44,-28,-26,-32,-25,-36,-37,]),'CASE':([3,4,5,6,7,8,9,10,11,12,13,14,24,27,28,29,31,32,40,41,43,45,46,47,51,52,53,54,55,56,57,58,59,70,71,72,73,74,89,90,91,93,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,127,139,142,144,157,158,159,161,162,165,169,170,176,185,186,193,194,195,],[-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-57,-2,-15,-57,-57,-57,-55,-56,-16,-81,-57,-57,-77,-78,-79,-80,-82,-83,-22,-23,-57,-57,-57,-74,-75,-19,-20,-72,-73,-43,-57,-17,-18,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,146,-54,146,-31,-34,-24,-27,-30,-29,-35,-45,-44,-28,-26,-32,-25,-36,-37,]),'PTCOMA':([15,24,29,31,32,45,46,47,51,52,53,54,55,56,59,63,64,70,71,72,73,90,91,107,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,],[28,41,41,41,41,-81,41,41,-77,-78,-79,-80,-82,-83,41,97,98,41,41,-74,-75,-72,-73,41,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,148,149,-39,-38,]),'IGUAL':([17,29,66,99,167,],[30,44,100,131,182,]),'INCREMENTO':([17,45,167,],[31,72,180,]),'DECREMENTO':([17,45,167,],[32,73,181,]),'PARENTESIS_ABRE':([17,18,19,20,21,23,25,30,34,35,36,38,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[33,34,35,36,37,39,42,50,50,50,50,67,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'NULL':([30,44,],[47,71,]),'MENOS':([30,34,35,36,39,44,45,46,48,49,50,51,52,53,54,55,56,60,61,62,68,70,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,90,91,92,97,98,100,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,131,132,146,150,164,182,188,],[48,48,48,48,48,48,-81,76,48,48,48,-77,-78,-79,-80,-82,-83,76,76,76,76,76,-74,-75,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-72,76,76,48,48,48,-58,-59,-60,-61,-62,-63,76,76,76,76,76,76,76,76,-76,76,76,48,76,48,76,76,48,76,]),'NOT':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'ENTERO':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'DECIMAL':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'TRUE':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'FALSE':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'CADENA':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CHART':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'PARENTESIS_CIERRA':([33,42,45,51,52,53,54,55,56,60,61,62,67,68,72,73,90,91,92,101,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,135,136,137,138,166,168,171,172,173,174,180,181,188,],[59,69,-81,-77,-78,-79,-80,-82,-83,94,95,96,102,107,-74,-75,-72,-73,125,133,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,-47,-49,-51,-53,179,183,-46,-48,-50,-52,-40,-41,-42,]),'MAS':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,75,-77,-78,-79,-80,-82,-83,75,75,75,75,75,-74,-75,-72,75,75,-58,-59,-60,-61,-62,-63,75,75,75,75,75,75,75,75,-76,75,75,75,75,75,75,]),'POR':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,77,-77,-78,-79,-80,-82,-83,77,77,77,77,77,-74,-75,-72,77,77,77,77,-60,-61,-62,-63,77,77,77,77,77,77,77,77,-76,77,77,77,77,77,77,]),'DIV':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,78,-77,-78,-79,-80,-82,-83,78,78,78,78,78,-74,-75,-72,78,78,78,78,-60,-61,-62,-63,78,78,78,78,78,78,78,78,-76,78,78,78,78,78,78,]),'POT':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,79,-77,-78,-79,-80,-82,-83,79,79,79,79,79,-74,-75,-72,79,79,79,79,79,79,-62,79,79,79,79,79,79,79,79,79,-76,79,79,79,79,79,79,]),'MODULO':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,80,-77,-78,-79,-80,-82,-83,80,80,80,80,80,-74,-75,-72,80,80,80,80,-60,-61,-62,-63,80,80,80,80,80,80,80,80,-76,80,80,80,80,80,80,]),'IGUALACION':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,81,-77,-78,-79,-80,-82,-83,81,81,81,81,81,-74,-75,-72,81,81,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,81,81,-76,81,81,81,81,81,81,]),'DIREFENCIACION':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,82,-77,-78,-79,-80,-82,-83,82,82,82,82,82,-74,-75,-72,82,82,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,82,82,-76,82,82,82,82,82,82,]),'MAYORQ':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,83,-77,-78,-79,-80,-82,-83,83,83,83,83,83,-74,-75,-72,83,83,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,83,83,-76,83,83,83,83,83,83,]),'MENORQ':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,84,-77,-78,-79,-80,-82,-83,84,84,84,84,84,-74,-75,-72,84,84,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,84,84,-76,84,84,84,84,84,84,]),'MAYORIGUAL':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,85,-77,-78,-79,-80,-82,-83,85,85,85,85,85,-74,-75,-72,85,85,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,85,85,-76,85,85,85,85,85,85,]),'MENORIGUAL':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,86,-77,-78,-79,-80,-82,-83,86,86,86,86,86,-74,-75,-72,86,86,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,86,86,-76,86,86,86,86,86,86,]),'OR':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,87,-77,-78,-79,-80,-82,-83,87,87,87,87,87,-74,-75,-72,-73,87,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,87,87,87,87,87,87,]),'AND':([45,46,51,52,53,54,55,56,60,61,62,68,70,72,73,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,129,130,132,150,164,188,],[-81,88,-77,-78,-79,-80,-82,-83,88,88,88,88,88,-74,-75,-72,-73,88,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,88,-71,-76,88,88,88,88,88,88,]),'DOSPUNTOS':([45,51,52,53,54,55,56,72,73,90,91,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,145,164,],[-81,-77,-78,-79,-80,-82,-83,-74,-75,-72,-73,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-70,-71,-76,163,178,]),'STRING':([67,153,154,155,156,],[103,103,103,103,103,]),'INT':([67,153,154,155,156,],[104,104,104,104,104,]),'CHAR':([67,153,154,155,156,],[105,105,105,105,105,]),'DOUBLE':([67,153,154,155,156,],[106,106,106,106,106,]),'LLAVE_ABRE':([69,94,95,96,102,133,175,179,183,],[108,126,127,128,134,151,184,187,189,]),'COMA':([135,136,137,138,],[153,154,155,156,]),'ELSE':([158,],[175,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,108,126,128,134,163,178,184,187,189,],[2,140,141,147,152,177,186,190,191,192,]),'instruccion':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[3,27,3,3,3,3,27,27,27,27,3,27,3,3,27,3,3,27,27,27,]),'variables':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'if':([0,2,108,126,128,134,140,141,147,152,163,175,177,178,184,186,187,189,190,191,192,],[5,5,5,5,5,5,5,5,5,5,5,185,5,5,5,5,5,5,5,5,5,]),'switch':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'while':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'for':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'funciones':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'print':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'break':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'main':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'funcion_void':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'llamada_fvoid':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'var':([0,2,108,126,128,134,140,141,147,152,163,177,178,184,186,187,189,190,191,192,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'finInstruccion':([24,29,31,32,46,47,59,70,71,107,],[40,43,57,58,74,89,93,109,110,139,]),'expresion':([30,34,35,36,39,44,48,49,50,75,76,77,78,79,80,81,82,83,84,85,86,87,88,97,98,100,131,146,182,],[46,60,61,62,68,70,90,91,92,111,112,113,114,115,116,117,118,119,120,121,122,123,124,129,130,132,150,164,188,]),'declaracionfor1':([37,],[63,]),'declaracionfor2':([37,],[64,]),'parametrosf':([67,153,154,155,156,],[101,171,172,173,174,]),'listacases':([127,],[142,]),'default':([127,142,],[143,160,]),'case':([127,142,],[144,161,]),'actualizacion':([148,149,],[166,168,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_inicio','grammar.py',268),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_main','grammar.py',272),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',278),
  ('instruccion -> variables','instruccion',1,'p_declaraciones','grammar.py',286),
  ('instruccion -> if','instruccion',1,'p_declaraciones','grammar.py',287),
  ('instruccion -> switch','instruccion',1,'p_declaraciones','grammar.py',288),
  ('instruccion -> while','instruccion',1,'p_declaraciones','grammar.py',289),
  ('instruccion -> for','instruccion',1,'p_declaraciones','grammar.py',290),
  ('instruccion -> funciones','instruccion',1,'p_declaraciones','grammar.py',291),
  ('instruccion -> print','instruccion',1,'p_declaraciones','grammar.py',292),
  ('instruccion -> break','instruccion',1,'p_declaraciones','grammar.py',293),
  ('instruccion -> main','instruccion',1,'p_declaraciones','grammar.py',294),
  ('instruccion -> funcion_void','instruccion',1,'p_declaraciones','grammar.py',295),
  ('instruccion -> llamada_fvoid','instruccion',1,'p_declaraciones','grammar.py',296),
  ('instruccion -> error PTCOMA','instruccion',2,'p_instruccion_error','grammar.py',300),
  ('variables -> var IDENTIFICADOR finInstruccion','variables',3,'p_variables1','grammar.py',305),
  ('variables -> var IDENTIFICADOR IGUAL expresion finInstruccion','variables',5,'p_declara','grammar.py',308),
  ('variables -> var IDENTIFICADOR IGUAL NULL finInstruccion','variables',5,'p_asginacionnula1','grammar.py',313),
  ('variables -> IDENTIFICADOR IGUAL expresion finInstruccion','variables',4,'p_asgina','grammar.py',317),
  ('variables -> IDENTIFICADOR IGUAL NULL finInstruccion','variables',4,'p_asginacionnula2','grammar.py',321),
  ('var -> VAR','var',1,'p_var','grammar.py',325),
  ('variables -> IDENTIFICADOR INCREMENTO finInstruccion','variables',3,'p_incrementa','grammar.py',328),
  ('variables -> IDENTIFICADOR DECREMENTO finInstruccion','variables',3,'p_decrementa','grammar.py',332),
  ('if -> IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','if',7,'p_if1','grammar.py',338),
  ('if -> IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE LLAVE_ABRE instrucciones LLAVE_CIERRA','if',11,'p_ifelse','grammar.py',343),
  ('if -> IF PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA ELSE if','if',9,'p_difelseif','grammar.py',348),
  ('switch -> SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases LLAVE_CIERRA','switch',7,'p_switch','grammar.py',354),
  ('switch -> SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE listacases default LLAVE_CIERRA','switch',8,'p_switch1','grammar.py',358),
  ('switch -> SWITCH PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE default LLAVE_CIERRA','switch',7,'p_switch2','grammar.py',362),
  ('listacases -> listacases case','listacases',2,'p_listacases1','grammar.py',366),
  ('listacases -> case','listacases',1,'p_listacases2','grammar.py',372),
  ('case -> CASE expresion DOSPUNTOS instrucciones','case',4,'p_cases','grammar.py',379),
  ('default -> DEFAULT DOSPUNTOS instrucciones','default',3,'p_defauult','grammar.py',383),
  ('main -> MAIN PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','main',6,'p_menu','grammar.py',388),
  ('while -> WHILE PARENTESIS_ABRE expresion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','while',7,'p_while','grammar.py',392),
  ('for -> FOR PARENTESIS_ABRE declaracionfor1 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','for',11,'p_for1','grammar.py',395),
  ('for -> FOR PARENTESIS_ABRE declaracionfor2 PTCOMA expresion PTCOMA actualizacion PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','for',11,'p_for2','grammar.py',400),
  ('declaracionfor1 -> VAR IDENTIFICADOR IGUAL expresion','declaracionfor1',4,'p_declaracionfor1','grammar.py',406),
  ('declaracionfor2 -> IDENTIFICADOR IGUAL expresion','declaracionfor2',3,'p_declaracionfor2','grammar.py',410),
  ('actualizacion -> IDENTIFICADOR INCREMENTO','actualizacion',2,'p_actualizacionfor1','grammar.py',414),
  ('actualizacion -> IDENTIFICADOR DECREMENTO','actualizacion',2,'p_actualizacionfor2','grammar.py',417),
  ('actualizacion -> IDENTIFICADOR IGUAL expresion','actualizacion',3,'p_actualizacionfor3','grammar.py',420),
  ('llamada_fvoid -> IDENTIFICADOR PARENTESIS_ABRE PARENTESIS_CIERRA finInstruccion','llamada_fvoid',4,'p_llamada','grammar.py',424),
  ('funcion_void -> FUNC IDENTIFICADOR PARENTESIS_ABRE PARENTESIS_CIERRA LLAVE_ABRE instrucciones LLAVE_CIERRA','funcion_void',7,'p_funcion_void','grammar.py',428),
  ('funciones -> FUNC IDENTIFICADOR PARENTESIS_ABRE parametrosf PARENTESIS_CIERRA LLAVE_ABRE LLAVE_CIERRA','funciones',7,'p_funciones','grammar.py',434),
  ('parametrosf -> STRING IDENTIFICADOR COMA parametrosf','parametrosf',4,'p_parametrosf','grammar.py',438),
  ('parametrosf -> STRING IDENTIFICADOR','parametrosf',2,'p_parametrosf','grammar.py',439),
  ('parametrosf -> INT IDENTIFICADOR COMA parametrosf','parametrosf',4,'p_parametrosf','grammar.py',440),
  ('parametrosf -> INT IDENTIFICADOR','parametrosf',2,'p_parametrosf','grammar.py',441),
  ('parametrosf -> CHAR IDENTIFICADOR COMA parametrosf','parametrosf',4,'p_parametrosf','grammar.py',442),
  ('parametrosf -> CHAR IDENTIFICADOR','parametrosf',2,'p_parametrosf','grammar.py',443),
  ('parametrosf -> DOUBLE IDENTIFICADOR COMA parametrosf','parametrosf',4,'p_parametrosf','grammar.py',444),
  ('parametrosf -> DOUBLE IDENTIFICADOR','parametrosf',2,'p_parametrosf','grammar.py',445),
  ('print -> PRINT PARENTESIS_ABRE expresion PARENTESIS_CIERRA finInstruccion','print',5,'p_print','grammar.py',448),
  ('break -> BREAK finInstruccion','break',2,'p_break','grammar.py',452),
  ('finInstruccion -> PTCOMA','finInstruccion',1,'p_finInstruccion','grammar.py',456),
  ('finInstruccion -> <empty>','finInstruccion',0,'p_finInstruccion','grammar.py',457),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',461),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',462),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',463),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','grammar.py',464),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',465),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_binaria','grammar.py',466),
  ('expresion -> expresion IGUALACION expresion','expresion',3,'p_expresion_binaria','grammar.py',467),
  ('expresion -> expresion DIREFENCIACION expresion','expresion',3,'p_expresion_binaria','grammar.py',468),
  ('expresion -> expresion MAYORQ expresion','expresion',3,'p_expresion_binaria','grammar.py',469),
  ('expresion -> expresion MENORQ expresion','expresion',3,'p_expresion_binaria','grammar.py',470),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',471),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',472),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',473),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',474),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',507),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',508),
  ('expresion -> IDENTIFICADOR INCREMENTO','expresion',2,'p_incremento','grammar.py',516),
  ('expresion -> IDENTIFICADOR DECREMENTO','expresion',2,'p_decremento','grammar.py',521),
  ('expresion -> PARENTESIS_ABRE expresion PARENTESIS_CIERRA','expresion',3,'p_expresion_agrupacionn','grammar.py',527),
  ('expresion -> ENTERO','expresion',1,'p_entero','grammar.py',531),
  ('expresion -> DECIMAL','expresion',1,'p_decimal','grammar.py',534),
  ('expresion -> TRUE','expresion',1,'p_true','grammar.py',537),
  ('expresion -> FALSE','expresion',1,'p_false','grammar.py',540),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_identificador','grammar.py',543),
  ('expresion -> CADENA','expresion',1,'p_cadena','grammar.py',546),
  ('expresion -> CHART','expresion',1,'p_chart','grammar.py',549),
]
