import ply.lex as lex

# List of token names
tokens = (
    'NUMBER', 'STRING', 'ID', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'VAR', 'IF', 'WHILE', 'PRINT', 'EXIT', 'SEMICOLON',
    'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r'='    # ✅ Fixed assignment operator
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMICOLON = r';'

# Relational operators
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'=='
t_NE = r'!='

# Reserved keywords
reserved = {
    'var': 'VAR',
    'if': 'IF',
    'while': 'WHILE',
    'print': 'PRINT',
    'exit': 'EXIT'
}

# Identifiers (variables)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Number handling
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String handling
def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # Remove surrounding quotes
    return t

# Ignored characters (spaces, tabs)
t_ignore = ' \t'

# Newline tracking
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
