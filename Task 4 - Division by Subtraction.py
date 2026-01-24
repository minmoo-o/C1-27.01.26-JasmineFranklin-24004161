number = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))

if divisor == 0:
    print("Cannot divide by zero")
else:
    count = 0
    remainder = number

    while remainder >= divisor: 
        remainder = remainder - divisor
        count = count + 1

    print("Result:", count)
    print("Remainder:", remainder)
