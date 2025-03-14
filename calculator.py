# Instructions:

# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

# Basic Calculator Program

def main():
    name = input("Hello! What is your name?\n ")
    print(f"Great to meet you, {name}. Let's do some math! ")
    
    while True:
        # Get user inputs
        num1 = float(input("What number would you like to start with?\n "))
        num2 = float(input("What is the second number you would like to use? \n"))
        operation = input("What operation would you like to perform? (+, -, *, /)\n ")
        
        
        # Perform calculation based on operation
        if operation == "+":
            result = num1 + num2 
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print(f"I'm sorry, you provided '{operation}' which is not a valid option. Please try again.")
        
        # Ask if user wants to continue
        choice = input("Would you like to try another calculation? (y (for yes)/n (for no)) \n")
        if choice.lower() != "y":
            print("Thank you for using the calculator. Goodbye!")
            break

# Execute the main function
if __name__ == "__main__":
    main()
