def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def remainder(a,b):
    return a%b
def exponent(a,b):
    return a**b

print("Choose your operation from the following")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divison")
print("5.Modulo")
print("6.Exponent")

operation = input("Enter your operation here :").lower()
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
if operation == "addition":
    ans = add(num1,num2)
    print(f"The answer is {ans}")
elif operation == "subtraction":
    ans = subtract(num1,num2)
    print(f"The answer is {ans}")
elif operation == "multiplication":
    ans = multiply(num1,num2)
    print(f"The answer is {ans}")
elif operation == "division":
    ans = divide(num1,num2)
    print(f"The answer is {ans}")
elif operation == "modulo":
    ans = remainder(num1,num2)
    print(f"The answer is {ans}")
elif operation == "exponent":
    ans = exponent(num1,num2)
    print(f"The answer is {ans}")
    
    
