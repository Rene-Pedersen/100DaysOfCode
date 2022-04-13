from Art import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    done = False
    while not done:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        want_more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if want_more == 'y':
            num1 = answer
        elif want_more == 'n':
            print("\n"*80)
            calculator()
        else:
            break


calculator()
