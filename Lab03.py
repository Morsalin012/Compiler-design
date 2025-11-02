import re
import os

KEYWORDS = [
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
]

OPERATORS = [
    "+", "-", "*", "/", "%",
    "=", "==", "!=", ">", "<",
    ">=", "<=", "&&", "||", "!",
    "+=", "-=", "*=", "/=", "%="
]

# The name of the file the program will attempt to read
FILE_NAME = "input.txt"

# Function to check if a token is a keyword
def is_keyword(token):
    return token in KEYWORDS

# Function to check if a token is an operator
def is_operator(token):
    return token in OPERATORS

# Function to check if a token is a number
def is_number(token):
    return bool(re.fullmatch(r'^-?\d+(\.\d+)?$', token))

def main():
    
    # --- File Reading Logic ---
    try:
        # Use 'with open' to ensure the file is closed automatically
        with open(FILE_NAME, 'r') as file:
            # Read the entire content of the file into a single string
            input_str = file.read()
    except FileNotFoundError:
        print(f"Error: The input file '{FILE_NAME}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return
    # --- End File Reading Logic ---

    # 1. Prepare the input string for tokenization
    
    # Remove all newline characters and replace ';' with a space
    s = input_str.replace('\n', ' ').replace('{', ' ').replace('}', ' ').replace(';', ' ').replace('(', ' ').replace(')', ' ')

    # Pad operators with spaces. Sorting by length ensures multi-character 
    # operators (like '>=') are replaced before single-character ones (like '>').
    for op in sorted(OPERATORS, key=len, reverse=True):
        # We replace the operator with itself surrounded by spaces
        s = s.replace(op, f" {op} ")

    # 2. Split the string by whitespace to get tokens
    # Using split() without arguments handles multiple spaces between tokens
    tokens = s.split()

    for token in tokens:
        if not token.strip(): # Skip empty strings resulting from multiple spaces
            continue
            
        if is_keyword(token):
            print("Token: {:<10} -> **Keyword**".format(token))
        elif is_operator(token):
            print("Token: {:<10} -> **Operator**".format(token))
        elif is_number(token):
            print("Token: {:<10} -> **Number**".format(token))
        else:
            # Assuming anything left is an identifier (variable name, etc.)
            print("Token: {:<10} -> **Identifier**".format(token))

if __name__ == "__main__":
    main()
