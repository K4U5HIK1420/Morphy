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
    'statement : PRINT LPAREN STRING RPAREN SEMICOLON'
    print(p[3])  # Print the string

def p_statement_if(p):
    'statement : IF LPAREN expression RPAREN LBRACE statements RBRACE'
    if p[3]:  # Execute block if condition is true
        for stmt in p[6]:
            stmt()

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

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    p[0] = variables.get(p[1], 0)  # Get variable value or default to 0

# Error handling
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()
