# hello.py
print("Hello, World!")
print("OM SARASWATHI DEVIYE NAMAHA,  om sairam")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    print("Welcome to the simple calculator!")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            operation = input("Enter operation (+, -, *, /) or 'q' to quit: ").strip()
            if operation == 'q':
                print("Goodbye!")
                break
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operation!")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()



