def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

if __name__ == "__main__":
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1-4): "))

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == 2:
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == 4:
        try:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        except ValueError as e:
            print(e)

    else:
        print("Invalid choice. Please enter a valid option (1-4).")
