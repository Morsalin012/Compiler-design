import re

# Keywords in C
keywords = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
}

# Operators in C
operators = {
    "+", "-", "*", "/", "%", "=", "==", "!=", ">", "<",
    ">=", "<=", "&&", "||", "!", "+=", "-=", "*=", "/=", "%="
}

def is_keyword(token: str) -> bool:
    return token in keywords

def is_operator(token: str) -> bool:
    return token in operators

def is_number(token: str) -> bool:
    try:
        float(token)
        return True
    except ValueError:
        return False

def main():
    # Ask user for text filename
    filename = input("Enter the text filename (e.g., code.txt): ")

    try:
        with open(filename, "r") as file:
            input_code = file.read()
    except FileNotFoundError:
        print("Error: File not found!")
        return

    # Tokenize using regex
    tokens = re.findall(r"[A-Za-z_]\w*|\d+\.\d+|\d+|==|!=|>=|<=|\+=|-=|\*=|/=|%=|[+\-*/%=><!;]", input_code)

    # Process tokens
    for token in tokens:
        if is_keyword(token):
            print(f"Token: {token} -> Keyword")
        elif is_operator(token):
            print(f"Token: {token} -> Operator")
        elif is_number(token):
            print(f"Token: {token} -> Number")
        elif token == ";":
            continue  # ignore semicolons
        else:
            print(f"Token: {token} -> Identifier")

if __name__ == "__main__":
    main()
