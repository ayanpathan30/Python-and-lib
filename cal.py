#PYTHON CODE FOR CALCULATOR
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
         return a / b
# Menu for Calculator
def calculator():
    print("Welcome to the Calculator Program!")
    print("Select an operation:")
    print("1. Add")   
    print("2. Subtract")  
    print("3. Multiply")   
    print("4. Divide")
    # Taking user input
    choice = input("Enter the operation number (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        except ValueError:
            print("Error! Please enter valid numbers.")
    else:
        print("Invalid operation! Please choose between 1 and 4.")
# Run the calculator
calculator()

