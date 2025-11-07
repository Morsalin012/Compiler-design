ALLOWED = "0123456789+-*/() "

def basic_validation(expr):
    # every char must be in allowed
    for ch in expr:
        if ch not in ALLOWED:
            return False
    return True


def operator_placement_validation(expr):
    expr = expr.replace(" ", "")
    ops = "+-*/"

    # cannot start or end with operator
    if expr[0] in ops or expr[-1] in ops:
        return False

    # cannot have two operators next to each other
    for i in range(len(expr)-1):
        if expr[i] in ops and expr[i+1] in ops:
            return False

    # cannot have ) after operator
    for i in range(len(expr)-1):
        if expr[i] in ops and expr[i+1] == ')':
            return False

    return True


def main():
    expr = input("Enter expression: ")

    if not basic_validation(expr):
        print("Invalid (bad characters)")
        return

    if not operator_placement_validation(expr):
        print("Invalid (operator problem)")
    else:
        print("Valid Expression")


if __name__ == "__main__":
    main()
