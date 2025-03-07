import ply.yacc as yacc
from lexer import tokens

# Symbol table to store variables
variables = {}

# Grammar rules
def p_statement_var_assign(p):
    'statement : VAR ID ASSIGN expression SEMICOLON'
    variables[p[2]] = p[4]

def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    if p[1] in variables:
        variables[p[1]] = p[3]
    else:
        print(f"Error: Variable '{p[1]}' is not declared.")

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMICOLON'
    print(p[3])  # Print the evaluated expression

def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN LBRACE statements RBRACE'
    if p[3]:  # If condition is true, execute block
        for stmt in p[6]:  
            execute_statement(stmt)

# Function to execute statements properly
def execute_statement(stmt):
    if isinstance(stmt, str):  
        print(stmt)
    elif callable(stmt):  
        stmt()
    elif isinstance(stmt, tuple) and len(stmt) == 2:
        var_name, value = stmt
        variables[var_name] = value

def p_statements_multiple(p):
    'statements : statements statement'
    p[0] = p[1] + [p[2]]  

def p_statements_single(p):
    'statements : statement'
    p[0] = [p[1]]  

# Expression handling
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_relational(p):
    '''expression : expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression'''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_expression_logic_and_or(p):
    '''expression : expression AND expression
                  | expression OR expression'''
    if p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]

def p_expression_logic_not(p):
    'expression : NOT expression'
    if isinstance(p[2], bool):  # ✅ Ensure it's a boolean
        p[0] = not p[2]
    else:
        print("Error: NOT operator expects a boolean value.")
        p[0] = False  # Default to False in case of an error

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = variables.get(p[1], 0)  

# Boolean literals
def p_expression_true(p):
    'expression : TRUE'
    p[0] = True

def p_expression_false(p):
    'expression : FALSE'
    p[0] = False

# Operator precedence
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),  
    ('nonassoc', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NE'),  
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
