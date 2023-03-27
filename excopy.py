# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ELEMENTO',
   'ELEMENTOQUIM',
   'VALENCIA',
   'COMPUESTO',
   'COMPUESTOS',
   'ENLACE'
)

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ELEMENTOQUIM = r'(H|Li|Na|S|Cl)'
t_ENLACE = r'-|=|:{1,2}'
t_VALENCIA = r'[1-9]+'
t_ELEMENTO = t_ELEMENTOQUIM + t_VALENCIA
#t_COMPUESTO =  t_ELEMENTOQUIM + t_ELEMENTO + r'[' + t_ENLACE + r']+' + r'|' + t_ELEMENTOQUIM + t_ELEMENTO + r'|' + t_ELEMENTOQUIM + t_ELEMENTOQUIM
#t_COMPUESTOS = t_COMPUESTO + t_COMPUESTO + r'|' + t_COMPUESTO 
t_COMPUESTO =  t_ELEMENTOQUIM + t_ELEMENTO + r'[' + t_ENLACE + r']+' + r'|' + t_ELEMENTOQUIM + t_ELEMENTO
t_COMPUESTOS = r'(' + t_COMPUESTO +r')+' + t_ELEMENTO + r'|' + r'(' + t_COMPUESTO +r')' + t_ELEMENTOQUIM 

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
Na
Na1
NaCl
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(f'Token: {tok.type} | Value: {tok.value}')
    