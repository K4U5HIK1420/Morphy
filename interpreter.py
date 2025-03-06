from parser_1 import parser

print("MiniLang Interpreter (Type 'exit' to quit)")

while True:
    try:
        text = input("MiniLang > ")
        if text.strip().lower() == 'exit':
            break
        parser.parse(text)
    except EOFError:
        break
