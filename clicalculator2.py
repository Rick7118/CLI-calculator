def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b): return a/b
def remainder(a,b): return a%b
def exponent(a,b): return a**b

# Master dictionary with both numbers and names as keys
operations = {
    "1": add, "addition": add,
    "2": subtract, "subtraction": subtract,
    "3": multiply, "multiplication": multiply,
    "4": divide, "division": divide,
    "5": remainder, "modulo": remainder,
    "6": exponent, "exponent": exponent
}

print("Choose your operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Exponent")

operation = input("Enter your choice (number or name): ").lower()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation in operations:
    ans = operations[operation](num1, num2)
    print(f"The answer is {ans}")
else:
    print("Invalid operation lodu")
