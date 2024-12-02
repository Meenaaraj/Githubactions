def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def perform_operations():
    print("Simple Calculator Results:")
    # Define some example calculations
    print(f"Addition: 10 + 5 = {add(10, 5)}")
    print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
    print(f"Division: 10 / 5 = {divide(10, 5)}")
    print(f"Division by zero: 10 / 0 = {divide(10, 0)}")


if __name__ == "__main__":
    # Automatically perform calculations
    perform_operations()
