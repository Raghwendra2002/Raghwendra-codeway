
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y

print("Welcome to Simple Calculator")

while True:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        print("Result:", add(num1, num2))
    elif operator == '-':
        print("Result:", subtract(num1, num2))
    elif operator == '*':
        print("Result:", multiply(num1, num2))
    elif operator == '/':
        
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result:", divide(num1, num2))
    else:
        print("Invalid operator!")

    
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break

print("Thank you for using Simple Calculator!")