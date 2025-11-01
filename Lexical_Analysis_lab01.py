import re
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
# Function to check if a token is a keyword
def is_keyword(token):
    """Checks if the given token is a C keyword."""
    return token in KEYWORDS

# Function to check if a token is an operator
def is_operator(token):
    """Checks if the given token is a C operator."""
    return token in OPERATORS

# Function to check if a token is a number
def is_number(token):
    """Checks if the given token is an integer or a floating-point number."""
    # Use a regular expression to match integers and floating-point numbers
    # This is generally more robust than manual character checking in C
    return bool(re.fullmatch(r'^-?\d+(\.\d+)?$', token))

def main():
    # Fixed input (string to be tokenized)
    input_str = "int a = 5; float b = a + 3.14"

    # 1. Prepare the input string to separate identifiers/keywords/numbers
    #    from operators and delimiters.
    # We replace common delimiters (like ';') and pad operators with spaces
    # so they get split correctly when using split().

    # A more complete lexical analyzer would use a proper state machine,
    # but to closely mimic the C code's simple `strtok` approach:
    
    # Replace ';' with a space
    s = input_str.replace(';', ' ')

    # Pad operators with spaces to ensure they are isolated tokens
    # Note: This is an oversimplification and might break multi-character
    # operators if not done carefully, but it works for this specific input.
    for op in sorted(OPERATORS, key=len, reverse=True):
        # Only replace operators that are NOT part of a number (like in 3.14)
        # This simple approach doesn't handle that perfectly, but we proceed
        # with the direct replacement as in the C code's concept.
        s = s.replace(op, f" {op} ")

    # 2. Split the string by whitespace to get tokens
    tokens = s.split()

    # 3. Classify and print each token
    print("Input: \"{}\"".format(input_str))

    for token in tokens:
        if is_keyword(token):
            print("Token: {} **Keyword**".format(token))
        elif is_operator(token):
            print("Token: {} **Operator**".format(token))
        elif is_number(token):
            print("Token: {} **Number**".format(token))
        else:
            # Assuming anything left is an identifier (variable name, etc.)
            print("Token: {} **Identifier**".format(token))

if __name__ == "__main__":
    main()