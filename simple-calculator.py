while True:
    print("Enter first number (or type 'done' to exit):")
    first_input = input()

    if first_input.lower() == "done":
        print("Calculator closed.")
        break

    num1 = float(first_input)

    print("Enter second number:")
    num2 = float(input())

    print("Enter operator:")
    operator = input()

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
print("Result:", result)
#test git