from anLexico import tokens
import ply.yacc as yacc

#Crear regla de consulta simple
#Crear regla de consulta con where
#Crear regla para anidar condiciones
#Crear regla para comparadores
#Crear regla para anidar campos
#Crear una regla padre que permita llamar a las 4 operaciones


#Kevin Castro
#estructura dd control
def p_while(p):
  'ejec : WHILE LPAREN ID comparation INT RPAREN FUNSEP option FUNSEP'

#estructura de datos
def p_classD(p):
  'ejec : CLASS ID FUNSEP atribC FUNSEP'


def p_atrib(p):
  'atrib : vas ID DOUBLEP TYPEDATA EQUALS data'


def p_comparation(p):
  '''comparation : EQUALS
  | GREATERTHAN
  | LESSTHAN
  '''


def p_print(p):
 'print : PRINTLN LPAREN data RPAREN'

def p_printDW(p):
  '''printDW : print 
  | print printDW
  '''
#declaracion de funcion
def p_Sfunction(p):
  'ejec : FUN ID LPAREN funcionparametro RPAREN DOUBLEP data FUNSEP RETURN ID FUNSEP'


def p_dataT(p):
  '''data : INT
  | CHAR
  | FLOAT
  | STR
  '''

def p_atribC(p):
  ''' atribC : atrib
  | atrib atribC
  '''
def p_option(p):
  '''option : assignment
  | assignmentL 
  | printDW
  '''
def p_Cif(p): 
  'ejec : IF LPAREN ID comparation INT RPAREN FUNSEP option FUNSEP'

def p_elif(p):
  'ejec : IF LPAREN ID comparation INT RPAREN FUNSEP option FUNSEP ELSE FUNSEP option FUNSEP' 
  
  
  
def p_assignment(p):
  'assignment : vas ID EQUALS data'


def p_assignmentL(p):
  'assignmentL : assignmentL assignment'


def p_assinmentLU(p):
  'assignmentL : assignment'


def p_vas(p):
  '''vas : VAL
  | VAR
  '''


#Giancarlo Ortiz


#for (i in 2){}
def p_for1(p):
  'ejec : FOR LPAREN ID IN INT RPAREN FUNSEP FUNSEP'


# val nombres: List<String> = listOf("Juan", "María", "Pedro",....)
# val nombres: List<int> = listOf(1,2,3,4,....)
def p_lista1(p):
  'ejec : VAL ID DOUBLEP LIST LESSTHAN liststring RPAREN'


def p_liststring(p):
  ''' liststring : STRING GREATERTHAN EQUALS listof LPAREN listadostringproduccion
  | INT GREATERTHAN EQUALS listof LPAREN listadointproduccion
  '''


def p_listadostring(p):
  'listadostring : STR'


def p_listadostringproduccion(p):
  ''' listadostringproduccion : listadostring
  | listadostring COMMA listadostringproduccion 
  '''


def p_listadoint(p):
  'listadoint : INT'


def p_listadointproduccion(p):
  ''' listadointproduccion : listadoint
  | listadoint COMMA listadointproduccion
  '''


#fun nombreFuncion(parametro1: Tipo, parametro2: Tipo): Unit {}
def p_funcion(p):
  'ejec : FUN ID LPAREN funcionproduccion RPAREN DOUBLEP UNIT FUNSEP FUNSEP'


def p_funcionparametro(p):
  ''' funcionparametro : ID DOUBLEP funciondato
  '''


def p_funciondato(p):
  ''' funciondato : STRING 
  | INTEGER
  '''


def p_funcionproduccion(p):
  ''' funcionproduccion : funcionparametro
  | ID DOUBLEP funciondato COMMA funcionproduccion
  '''


def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
#sintactico.errok()
  else:
    print("Syntax error at EOF")



#Steven Choez
#Estructura de control - ForEach
#For Each: list.forEach {(it)}
def p_forEach(p):
    'ejec : ID DOT FOR EACH FUNSEP PRINTLN LPAREN ID RPAREN FUNSEP'

#Estructura de datos - Diccionario o Mapa
#Map<String, Int> = mapOf( Pair("Num1", 1), Pair("Num2", 2), Pair("Num3", 3))
def p_map(p):
    '''ejec : MAP LESSTHAN TYPEDATA COMMA TYPEDATA GREATERTHAN EQUALS MAP OF LPAREN pares RPAREN'''

def p_pares(p):
    '''pares : pair
    | pair COMMA pares
             '''

def p_pair(p):
    '''pair : PAIR LPAREN data COMMA data RPAREN'''

#def p_data(p):
#    '''data : TYPEDATA'''

#def p_data(p):
#    '''data : STR
#            | INT'''   

#Función con parámetro preterminado
#fun nombreFuncion(parametro1: Tipo, parametro2: Tipo = valorPredeterminado) { codigo }
def p_ejec(p):
    '''ejec : function'''

def p_function(p):
    '''function : FUN ID LPAREN params RPAREN DOUBLEP FUNSEP'''
  
def p_params(p):
    '''params : param
              | param COMMA params'''

def p_param(p):
    '''param : ID DOUBLEP TYPEDATA
             | ID DOUBLEP TYPEDATA EQUALS data'''

#Función
def p_funUE(p):
  'ejec : FUN ID LPAREN funcionproduccion RPAREN DOUBLEP TYPEDATA EQUALS assignment'



# Build the parser
sintactico = yacc.yacc()

while True:
  try:
    s = input('sql > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(s)
  if result != None:
    print(result)
