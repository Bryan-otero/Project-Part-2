# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN
import sys

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'FIN_DE_LINEA',
   'LETRA',
   'DIGITO',
   'TIPO',
   'OPERACION',
   'VALENCIA',
   'ELEMENTO',
   'ELEMENTO_QUIMICO',
   'ENLACE',
   'ID',
   'IDCONT',
   'SENTENCIAS',
   'SENTENCIA',
   'MODELO_MOLECULAR',
   'COMPUESTO',
   'COMPUESTOS',
   'GRUPO_FUNCIONAL',
   'GRUPO_FUNCIONAL_INFERIOR',
   'GRUPO_FUNCIONAL_SUPERIOR',
   'MODELO_GRUPO_FUNCIONAL'
)

# Regular expression rules for simple tokens

# t_LETRA = r'\w+'
# t_DIGITO = r'\d+'
# t_IDCONT = t_LETRA + r'|' + r'(' + t_LETRA + r')' + t_LETRA + r'|' + t_DIGITO + r'|' + r'(' + t_DIGITO + r')' + t_LETRA 
# t_ID = r'^(' + t_LETRA + r')' + t_IDCONT + r'?' + r'|' + t_LETRA

# t_MODELO_GRUPO_FUNCIONAL = r''
# t_GRUPO_FUNCIONAL_INFERIOR = r'^\[{1}' + +  r'\]{1}?'
# t_GRUPO_FUNCIONAL_SUPERIOR = r''
# t_GRUPO_FUNCIONAL = r''


t_VALENCIA = r'[1-9]{1}'
t_ENLACE = r'(-|=|:{1,2})'

t_ELEMENTO_QUIMICO = r'H|Li|Na|K|Rb|Cs|Fr|Be|Mg|Ca|Sr|Ba|Ra|Sc|Y|Ti|Zr|Hf|Db|V|Nb|Ta|Jl|Cr|Mo|W|Rf|Mn|To|Re|Bh|Fe|Ru|Os|Hn|Co|Rh|Ir|Mt|Ni|Pd|Pt|Cu|Ag|Au|Zn|Cd|Hg|B|Al|Ga|In|Tl|Cl|Si|Ge|Sn|Pb|N|P|As|Sb|Bi|O|S|Se|Te|Po|F|C|Br|I|At|He|Ne|Ar|Kr|Xe|Rn'
#t_ELEMENTO_QUIMICO = r'B'
t_ELEMENTO =  r'(' + t_ELEMENTO_QUIMICO + r')' + t_VALENCIA + r'|' + t_ELEMENTO_QUIMICO 
t_COMPUESTO = r'(' + t_ELEMENTO + r')' + t_ENLACE + r'+'
t_COMPUESTOS = r'(' + t_COMPUESTO + r')+' + r'(' + t_ELEMENTO + r')+' + t_ENLACE + r'{0,1}'

#t_GRUPO_FUNCIONAL_INFERIOR = r'^\[{1}' +  t_ELEMENTO +  r'\]{1}?'
t_GRUPO_FUNCIONAL_INFERIOR = r'\[' + r'(' + t_COMPUESTO + r')' + r'\]' + r'|' + r'\[' + r'(' + t_ELEMENTO + r')' + r'\]'
t_GRUPO_FUNCIONAL_SUPERIOR = r'\(' + r'(' + t_COMPUESTO + r')' + r'\)' + r'|' + r'\(' + r'(' + t_ELEMENTO + r')' + r'\)'
t_GRUPO_FUNCIONAL = r'(' + r'(' + t_GRUPO_FUNCIONAL_SUPERIOR + r')+' + r'(' + t_GRUPO_FUNCIONAL_INFERIOR + r')+' + r')' + r'|' r'(' + r'(' + t_GRUPO_FUNCIONAL_INFERIOR + r')+' + r'(' + t_GRUPO_FUNCIONAL_SUPERIOR + r')+' + r')'


 

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
    
#Read from .txt file
myFile = open(sys.argv[1])
 
lexer = lex.lex()
 
with myFile as fp:
    for line in fp:
        try:
            lexer.input(line)
 
            for token in lexer:
                print(f'Token: {token.type} | Value: {token.value}')
 
        except EOFError:
            break
    