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
   'LETRA',
   'DIGITOS',
   'ID',
   'IDCONT'
)

# Regular expression rules for simple tokens
t_LETRA = r'\w+'
t_DIGITOS = r'\d+'
t_IDCONT = t_LETRA + r'|' + r'(' + t_LETRA + r')' + t_LETRA + r'|' + t_DIGITOS + r'|' + r'(' + t_DIGITOS + r')' + t_LETRA 
t_ID = t_LETRA + r'|' + r'(' + t_LETRA + r')' + t_IDCONT

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
Bryan
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(f'Token: {tok.type} | Value: {tok.value}')
    