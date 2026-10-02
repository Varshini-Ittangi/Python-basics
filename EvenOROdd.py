# Check if a number is odd or even using modulo operator
# Using while True to repeatedly ask for input until the program is stopped

while True:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("{num} is Even")
    else:
        print("{num} is Odd")
