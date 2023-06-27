import ply.lex as lex
#Analizador léxico de Kotlin
#Crear los tokens para los siguiente algoritmos

#Algoritmo de Kevin Castro
#Buca un caracter en una cadena
""""fun buscarCaracter(cadena: String, caracter: Char): Boolean {
    for (c in cadena) {
        if (c == caracter) {
            #return true
        }
    }
  return false
}

fun main() {
    val cadena = "Hola, mundo!"
    val caracter = 'a'
    
    val encontrado = buscarCaracter(cadena, caracter)
    
    if (encontrado) {
        println("El caracter se encontró en la cadena.")
    } else {
        println("El caracter no se encontró en la cadena.")
    }
}"""

#Algoritmo de Giancarlo Ortiz
#Operaciones Matemáticas y Manipulación de Valores Nulos
"""
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)
    val squaredNumbers = numbers.map { it * it }
    println("Squared numbers: $squaredNumbers")

    val filteredNumbers = squaredNumbers.filter { it % 2 == 0 }
    println("Filtered numbers: $filteredNumbers")

    val sum = filteredNumbers.reduce { acc, value -> acc + value }
    println("Sum of filtered numbers: $sum")

    val result = numbers
        .filter { it % 2 != 0 }
        .map { it * it }
        .take(3)
        .joinToString(separator = ", ")
    println("Result: $result")

    val nullableValue: String? = null
    val length = nullableValue?.length ?: -1
    println("Length: $length")
}
"""

#Algoritmo de Steven Choez
"""fun bubbleSort(numbers: IntArray) { 
    val n = numbers.size 
 
    for (i in 0 until n - 1) { 
        for (j in 0 until n - i - 1) { 
            if (numbers[j] < numbers[j + 1]) { 
                // Intercambiar elementos 
                val temp = numbers[j] 
                numbers[j] = numbers[j + 1] 
                numbers[j + 1] = temp 
            } 
        } 
    } 
} 
 
fun main() { 
    val numbers = intArrayOf(5, 2, 8, 1, 9) 
 
    println("Números sin ordenar:") 
    numbers.forEach { print("$it ") } 
 
    bubbleSort(numbers) 
 
    println("\nNúmeros ordenados de mayor a menor:") 
    numbers.forEach { print("$it ") } 
}"""
#Diccionario de palabras reservadas
reserved = {
  'while': 'WHILE',
  'println': 'PRINTLN',
  #Kevin Castro
  'return': 'RETURN',
  'else': 'ELSE',
  'if': 'IF',
  'fun': 'FUN',
  'true': 'TRUE',
  #'false': 'FALSE',
  'var': 'VAR',
  'val': 'VAL',
  'for': 'FOR',
  #Giancarlo Ortiz
  'unit': 'UNIT',
  'integer': 'INTEGER',
  'string': 'STRING',
  #'public': 'PUBLIC',
  #'private': 'PRIVATE',
  #'protected': 'PROTECTED',
  'class': 'CLASS',
  'in': 'IN',
  #'not': 'NOT',
 # 'const': 'CONST',
  #'main': 'MAIN',
  'map': 'MAP',
  'list': 'LIST',
  'listof': 'listof',
  #'reduce': 'REDUCE',
  #'take': 'TAKE',
 # 'joinToString': 'JOINTOSTRING',
  #'input': 'INPUT',
  'in': 'IN',
  'DownTo': 'DownTo',
  #Steven Choez
  'print': 'PRINT',
  'length': 'LENGTH',
  'null': 'NULL',
  #'nullablevalue': 'NULLABLEVALUE',
  'foreach': 'FOREACH',
 # 'until': 'UNTIL',
  #'intArrayOf': 'INTARRAYOF',
  'each': 'EACH',
  'dictionary': 'DICTIONARY',
  'arrow': 'ARROW',
  'pair': 'PAIR',
  'of': 'OF',
  'dot': 'DOT',
}

#Sequencia de tokens, puede ser lista o tupla
tokens = (
  'INT',
  'FLOAT',
  #'PLUS',
  #'MINUS',
  #'TIMES',
  #'DIVIDE',
  'LPAREN',
  'RPAREN',
  'COMMA',
  #'DIFFERENT',
  'EQUALS',
  #'EQUALSC',
  'GREATERTHAN',
  'LESSTHAN',
  'ID',
  #Kevin Castro
  'TYPEDATA',
  'FUNSEP',
  'CHAR',
  'DOUBLEP',
  'STR',
  #'DOLAR',
  #Giancarlo Ortiz
  #'TYPESTRING',
  #'INCREMENTO',
 # 'DISMINICION',
  #'CONJ',
 # 'DISJ',
  #'ADD_ASSIGNMENT',
 # 'PUNTO',
  #'MODULO',
 # 'NEGACION',
  #Steven Choez
  'LBRACKET',
  'RBRACKET',
  'LLLAVE',
  'RLLAVE',
  #'NULLABLE',
) + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
#t_PLUS = r'\+'
#t_MINUS = r'-'
#t_TIMES = r'\*'
#t_DIVIDE = r'/'
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_COMMA = r','
#t_DIFFERENT = r'<>'

#Kevin Castro
t_FUNSEP = r'\}|\{'
t_TYPEDATA = r'String|Boolean|Char|Float|Int'
t_CHAR = r'\w'
t_DOUBLEP = r'\:'
t_INT = r'\d+'
t_FLOAT = r'-?\d*\.\d+'
t_STR = r'(\"|\')(.*?)(\"|\')'
#t_DOLAR = r'\$'
#Giancarlo Ortiz
#t_TYPESTRING = r'String'
#t_INCREMENTO = r'\+\+'
#t_DISMINICION = r'--'
#t_CONJ = r'&&'
#t_DISJ = r'\|\|'
#t_ADD_ASSIGNMENT = r'\+='
#t_PUNTO = r'\.'
#t_MODULO = r'\%'
#t_NEGACION = r'\!\='

#Steven Choez
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
#t_NULLABLE = '\?'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
#t_EQUALSC = r'=='


#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_ID(t):
  r'[a-zA-Z_]\w+'
  t.type = reserved.get(t.value.lower(), 'ID')
  return t


# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


def t_COMMENTS(t):
  r'\#.*'
  pass


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


#Contruir analizador
lexer = lex.lex()

#Testeando   También agregar algoritmos aquí
data = ''' 
fun main() {
    val numbers = listOf(1, 2, 3, 4, 5)
    val squaredNumbers = numbers.map { it * it }
    println("Squared numbers: $squaredNumbers")

    val filteredNumbers = squaredNumbers.filter { it % 2 == 0 }
    println("Filtered numbers: $filteredNumbers")

    val sum = filteredNumbers.reduce { acc, value -> acc + value }
    println("Sum of filtered numbers: $sum")

    val result = numbers
        .filter { it % 2 != 0 }
        .map { it * it }
        .take(3)
        .joinToString(separator = ", ")
    println("Result: $result")

    val nullableValue: String? = null
    val length = nullableValue?.length ?: -1
    println('Length: $length')
}
'''

#Datos de entrada
#lexer.input(data)

#Tokenizador
#while True:
#tok = lexer.token()
#if not tok:
#break  #Rompe
#print(tok)
