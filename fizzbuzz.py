#fizzbuzz

number = int(input("What is your number: "))

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "No FizzBuzz"

print(fizzbuzz(number))
