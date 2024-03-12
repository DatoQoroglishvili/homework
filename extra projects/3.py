
import math

def add(x, y):
    """
    Add two numbers.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.
    """
    return x * y

def divide(x, y):
    """
    Divide two numbers.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def square_root(x):
    """
    Calculate the square root of a number.
    """
    return math.sqrt(x)

def main():
    """
    The main function implementing the math program logic.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = add(num1, num2)
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtract(num1, num2)
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiply(num1, num2)
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            return
    elif choice == '5':
        num = float(input("Enter a number: "))
        try:
            result = square_root(num)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid input")
        return

    print(f"The result is {result}")


if __name__ == "__main__":
    main()