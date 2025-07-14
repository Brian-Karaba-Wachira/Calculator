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

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

def calculator():
    print("=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def main():
    while True:
        calculator()
        
        # Get operation choice
        try:
            choice = int(input("Choose operation (1-5): "))
            if choice < 1 or choice > 5:
                print("Error: Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        # Exit if chosen
        if choice == 5:
            print("Thank you for using the calculator!")
            break
        
        # Get numbers
        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")
        
        # Perform operation
        try:
            if choice == 1:
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask to continue
        while True:
            cont = input("Continue? (y/n): ").lower()
            if cont in ['y', 'n']:
                break
            print("Error: Please enter 'y' or 'n'.")
        
        if cont == 'n':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()