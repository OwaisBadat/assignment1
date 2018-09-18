#even_or_odd
print ("Even or odd? I'll tell you!")
print ("---------------------------")
number = int(input("What is your number: "))

def even_or_odd(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(even_or_odd(number))
