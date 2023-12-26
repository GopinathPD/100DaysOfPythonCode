from replit import clear
from art import logo

#Calculator Core functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Dictionary of operations with core functions
operations = {"+": add, 
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculator():

    #print logo
    print(logo)
    
    #Get the user input
    num1 = float(input("What's the first number?: "))
    
    
    for symbol in operations:
        print(symbol)
    
    calc_continue = True
    
    
    while calc_continue:
        operation_symbol = input("Pick an operation from the line above: 
")
        num2 = float(input("What's the next number?: " ))
        #Get the function from the dictionary
        calculation_function = operations[operation_symbol]
        #Calculate
        result = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        user_input = input(f"Type 'y' to continue calculating with 
{result}, type 'n' to start a new calculation, or type 'x' to exit.: ")
        if user_input.lower() == "y":
            num1 = result
        elif user_input.lower() == "n":
            calc_continue = False
            clear()
            calculator()
        elif user_input.lower() == "x":
            calc_continue = False
            print("Goodbye")
        else:
            print("Invalid input. Please try again.")

calculator()
