import math

# Calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Square root of negative numbers is not real!")
    return math.sqrt(a)

def percentage(a, b):
    """Calculate what percentage a is of b, or a% of b"""
    return (a * b) / 100

# History tracking
calculation_history = []

def add_to_history(operation, num1, num2=None, result=None):
    if len(calculation_history) >= 5:
        calculation_history.pop(0)
    
    if operation == '√':
        entry = f"√{num1} = {result}"
    elif operation == '%':
        entry = f"{num1}% of {num2} = {result}"
    else:
        entry = f"{num1} {operation} {num2} = {result}"
    
    calculation_history.append(entry)

def show_history():
    if not calculation_history:
        print("\nHistory is empty.")
    else:
        print("\n=== Calculation History ===")
        for i, entry in enumerate(calculation_history, 1):
            print(f"{i}. {entry}")

def clear_history():
    global calculation_history
    calculation_history = []
    print("\nHistory cleared.")

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def calculator_menu():
    print("\n=== Enhanced Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square root (√x)")
    print("7. Percentage (x% of y)")
    print("8. Show History")
    print("9. Clear History")
    print("10. Exit")

def main():
    while True:
        calculator_menu()
        
        # Get operation choice
        try:
            choice = int(input("\nChoose operation (1-10): "))
            if choice < 1 or choice > 10:
                print("Error: Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        # Handle non-calculation options
        if choice == 8:
            show_history()
            continue
        elif choice == 9:
            clear_history()
            continue
        elif choice == 10:
            print("\nThank you for using the calculator!")
            break
        
        # Get numbers based on operation
        try:
            if choice == 6:  # Square root only needs one number
                num1 = get_number_input("Enter number: ")
                num2 = None
            else:
                num1 = get_number_input("Enter first number: ")
                if choice == 7:  # Percentage
                    print("Note: This calculates x% of y")
                num2 = get_number_input("Enter second number: ")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            continue
        
        # Perform operation
        try:
            if choice == 1:
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
                add_to_history("+", num1, num2, result)
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
                add_to_history("-", num1, num2, result)
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
                add_to_history("*", num1, num2, result)
            elif choice == 4:
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
                add_to_history("/", num1, num2, result)
            elif choice == 5:
                result = power(num1, num2)
                print(f"\nResult: {num1}^{num2} = {result}")
                add_to_history("^", num1, num2, result)
            elif choice == 6:
                result = square_root(num1)
                print(f"\nResult: √{num1} = {result}")
                add_to_history("√", num1, None, result)
            elif choice == 7:
                result = percentage(num1, num2)
                print(f"\nResult: {num1}% of {num2} = {result}")
                add_to_history("%", num1, num2, result)
        except ValueError as e:
            print(f"\nError: {e}")
        
        # Ask to continue
        while True:
            cont = input("\nContinue? (y/n): ").lower()
            if cont in ['y', 'n']:
                break
            print("Error: Please enter 'y' or 'n'.")
        
        if cont == 'n':
            print("\nThank you for using the calculator!")
            break

if __name__ == "__main__":
    main()