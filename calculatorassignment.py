#calculator

from calculator import multiplication,division,addition,subtraction

first_number = int(input("Input your first number: "))
operand = input("Would you like to +, -, *, /:")
second_number = int(input("Input your second number: "))

if operand == "*":
    results = multiplication(first_number,second_number)
elif operand == "/":
    results = division(first_number,second_number)
elif operand == "+":
    results = addition(first_number,second_number)
elif operand == "-":
    results = subtraction(first_number,second_number)

print(results)
