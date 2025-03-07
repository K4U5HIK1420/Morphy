import ply.lex as lex

# List of token names
tokens = (
    'NUMBER', 'ID', 'STRING', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE',
    'AND', 'OR', 'NOT',
    'VAR', 'PRINT', 'IF', 'TRUE', 'FALSE'  # ✅ Added TRUE and FALSE tokens
)

# Reserved words
reserved = {
    'var': 'VAR',
    'print': 'PRINT',
    'if': 'IF',
    'true': 'TRUE',    # ✅ Define true
    'false': 'FALSE'   # ✅ Define false
}

# Regular expressions for tokens
t_ASSIGN   = r'='
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_SEMICOLON = r';'

# Relational Operators
t_GT       = r'>'
t_LT       = r'<'
t_GE       = r'>='
t_LE       = r'<='
t_EQ       = r'=='
t_NE       = r'!='

# Logical Operators
t_AND      = r'&&'
t_OR       = r'\|\|'
t_NOT      = r'!'

# Boolean literals
def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

# String handling
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove double quotes
    return t

# Identifier (variable names)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Number (integer only for now)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
