from ply import lex, yacc

tokens = (
    'INT', 'FLOAT', 'CHAR', 'ID',
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'EQUALS', 'INCREMENT', 'DECREMENT',
    'IF', 'WHILE', 'FOR',
    'LESSER', 'GREATER', 'LESSEREQUAL', 'GREATEREQUAL',
    'EQUALEQUAL', 'NOTEQUAL'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_EQUALS = r'='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSEREQUAL = r'<='
t_GREATEREQUAL = r'>='
t_EQUALEQUAL = r'=='
t_NOTEQUAL = r'!='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value == 'if': t.type = 'IF'
    elif t.value == 'while': t.type = 'WHILE'
    elif t.value == 'for': t.type = 'FOR'
    elif t.value == 'int': t.type = 'INT'
    elif t.value == 'float': t.type = 'FLOAT'
    elif t.value == 'char': t.type = 'CHAR'
    return t

def t_NUMBER(t):
    r'\d*\.?\d+'
    t.value = float(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def p_program(p):
    '''program : statement
               | program statement'''
    pass

def p_statement(p):
    '''statement : declaration
                | assignment
                | if_statement
                | while_statement
                | for_statement'''
    pass

def p_declaration(p):
    '''declaration : type ID SEMICOLON
                  | type ID EQUALS expression SEMICOLON'''
    pass

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    pass

def p_assignment(p):
    '''assignment : ID EQUALS expression SEMICOLON
                 | ID INCREMENT SEMICOLON
                 | ID DECREMENT SEMICOLON
                 | ID EQUALS expression'''  
    pass

def p_if_statement(p):
    '''if_statement : IF LPAREN condition RPAREN LBRACE program RBRACE'''
    pass

def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN LBRACE program RBRACE'''
    pass

def p_for_statement(p):
    '''for_statement : FOR LPAREN for_init condition SEMICOLON for_update RPAREN LBRACE program RBRACE'''
    pass

def p_for_init(p):
    '''for_init : declaration
                | assignment'''
    pass

def p_for_update(p):
    '''for_update : ID INCREMENT
                 | ID DECREMENT
                 | assignment'''
    pass

def p_condition(p):
    '''condition : expression comparison expression'''
    pass

def p_comparison(p):
    '''comparison : LESSER
                 | GREATER
                 | LESSEREQUAL
                 | GREATEREQUAL
                 | EQUALEQUAL
                 | NOTEQUAL'''
    pass

def p_expression(p):
    '''expression : term
                 | expression PLUS term
                 | expression MINUS term'''
    pass

def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''
    pass

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}'")
    else:
        raise SyntaxError("Syntax error at EOF")

lexer = lex.lex()
parser = yacc.yacc()

def test_code(code):
    print(f"\nTesting code:\n")
    try:
        parser.parse(code)
        print("Syntax is valid!")
    except SyntaxError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    while True:
        print("\nEnter your code (type 'END' to finish):")
        code_lines = []
        while True:
            line = input()
            if line.strip().lower() == 'end':
                break
            code_lines.append(line)
        
        code = "\n".join(code_lines)
        if code.strip().lower() == 'exit':
            break
        test_code(code)
